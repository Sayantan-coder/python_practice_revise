def upload_count(date_list: list, month: str) -> int:
    upload_count = 0
    for date in date_list:
        if month in date.split(" "):
            upload_count += 1
    return f"Youtube Upload Count for {month} mont is:{upload_count}"


print(upload_count(["Sept 22", "Sept 21", "Oct 15"], "Sept"))
print(upload_count(["Sept 22", "Sept 21", "Oct 15"], "Oct"))
print(upload_count(["Sept 22", "Sept 21", "Oct 15"], "Nov"))
