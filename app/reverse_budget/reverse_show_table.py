from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from aiogram import types
from db.search import SearchDB
from app.inline_button import back_menu

@RouterStore.my_router.callback_query(CallbackDataFilter("show_table"))
async def show_table(callback: types.CallbackQuery):
    LogCLassAll().debug('Press button: show_table')
    await callback.answer()
    await callback.message.delete()
    map_plan = await SearchDB().new_search_category_for_table(callback.from_user.id)
    full_table = await create_table(map_plan)
    await callback.message.answer(
        "*📊 Ваши категории и расходы:*\n" + full_table,
        parse_mode="MarkdownV2",
        reply_markup=back_menu())
    
    
async def create_table(map_plan: dict):
    sum_table = 0
    sum_plan = 0
    for i in map_plan:
        sum_table += i[1]
        sum_plan += i[2]
    table_header = "| Категория     | Осталось | Заложено | Потрачено|\n|---------------|----------|----------|----------|"
    table_end = f"| Осталось      | {sum_table}   | {sum_plan}   |"
    table_rows = []
    for category, amount, plan, difference in map_plan:
        row = f"| {(category.ljust(13)).capitalize()} | {str(amount).rjust(4)}   {str(plan).rjust(8)}   {str(difference).rjust(8)}\n|---------------|----------|----------|----------|"
        table_rows.append(row)
    full_table = f"```\n{table_header}\n" + "\n".join(table_rows) + f"\n{table_end}```"
    return full_table