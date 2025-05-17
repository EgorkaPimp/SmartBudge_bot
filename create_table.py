
async def create_table(map_plan):
    sum_table = 0
    for i in map_plan:
        sum_table += map_plan[i]
    table_header = "| Категория     | Сумма    |\n|---------------|----------|"
    table_end = f"| Осталось      | {sum_table}   |"
    table_rows = []
    for category, amount in map_plan.items():
        row = f"| {(category.ljust(13)).capitalize()} | {str(amount).rjust(8)} |\n|---------------|----------|"
        table_rows.append(row)
    full_table = f"```\n{table_header}\n" + "\n".join(table_rows) + f"\n{table_end}```"
    return full_table