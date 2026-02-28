import json
from typing import List, Dict, Any, Optional

logs = [
    "2025-02-01 10:15:33|INFO|user=anna action=login status=success ip=10.0.0.1",
    "2025-02-01 10:17:10|ERROR|user=bob action=payment status=fail amount=120",
    "2025-02-01 10:20:01|INFO|user=anna action=logout status=success",
    "2025-02-01 10:22:45|WARNING|user=anna action=payment status=fail amount=300",
    "2025-02-01 10:30:12|ERROR|user=tom action=login status=fail ip=10.0.0.5"
]

def try_parse_number(value: str) -> Any:
    """Attempts to convert a string to int or float, otherwise returns string."""
    clean_val = value.strip(" ,;")
    try:
        return int(clean_val)
    except ValueError:
        try:
            return float(clean_val)
        except ValueError:
            return clean_val

def parse_log_line(line: str) -> Optional[Dict[str, Any]]:
    """Parses a log line into a dict."""
    parts = line.split("|")
    if len(parts) < 3:
        return None

    date = parts[0].strip()
    level = parts[1].strip()
    message = parts[2].strip()

    data = {"date": date, "level": level}

    fields = message.split()
    for f in fields:
        if "=" in f:
            key, val = f.split("=", 1)
            data[key] = try_parse_number(val)
    return data

def process_logs(log_list: List[str], filename: Optional[str] = None) -> List[Dict[str, Any]]:
    parsed_results = []
    for line in log_list:
        if line.strip():
            parsed = parse_log_line(line)
            if parsed:
                parsed_results.append(parsed)
    if filename:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(parsed_results, f, indent=4, ensure_ascii=False)
    return parsed_results

def filter_logs(data: List[Dict[str, Any]], **criteria) -> List[Dict[str, Any]]:
    return [log for log in data if all(log.get(k) == v for k, v in criteria.items())]

def aggregate_by_field(data: List[Dict[str, Any]], field: str) -> Dict[Any, int]:
    counts = {}
    for log in data:
        val = log.get(field)
        if val is not None:
            counts[val] = counts.get(val, 0) + 1
    return counts

def calculate_failed_payment_total(data: List[Dict[str, Any]]) -> float:
    failed_payments = filter_logs(data, action="payment", status="fail")
    return sum(log.get("amount", 0) for log in failed_payments)

def main():
    parsed_logs = process_logs(logs, filename="output.json")
    print("---- PARSED LOGS (JSON) ----")
    print(json.dumps(parsed_logs, indent=2, ensure_ascii=False))
    
    print("\n---- FILTER: status=fail ----")
    for log in filter_logs(parsed_logs, status="fail"):
        print(log)

    print("\n---- ANALYTICS ----")
    level_counts = aggregate_by_field(parsed_logs, "level")
    user_counts = aggregate_by_field(parsed_logs, "user")
    failed_total = calculate_failed_payment_total(parsed_logs)
    
    print(f"Counts by level: {level_counts}")
    print(f"Counts by user:  {user_counts}")
    print(f"Total failed payment amount: {failed_total}")

if __name__ == "__main__":
    main()
