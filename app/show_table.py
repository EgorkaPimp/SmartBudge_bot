from aiogram import types
from BaseClass.start_class import RouterStore, CallbackDataFilter
from BaseClass.log_class import LogCLassAll
from db_postgres.crud.shares import status_share_search
from db_postgres.crud.utils import get_category_comparison
from app.inline_back import back_menu

@RouterStore.my_router.callback_query(CallbackDataFilter("show_table"))
async def show_table(callback: types.CallbackQuery):
    LogCLassAll().debug('Press button: show_table')
    await callback.answer()
    await callback.message.delete()
    
    master = await status_share_search(callback.from_user.id)
    if master:
        user_id = master.master_id
    else:
        user_id = callback.from_user.id
        
    plan = await get_category_comparison(user_id=user_id)
    full_table = await create_table(plan)
    await callback.message.answer(
        "*📊 Ваши категории и расходы:*\n" + full_table,
        parse_mode="MarkdownV2",
        reply_markup=back_menu())
    
async def create_table(map_plan: dict):
    sum_remaining = 0
    sum_plan = 0
    sum_exp = 0
    
    table_rows = []
    for cat in map_plan:
        sum_exp += cat['spent']
        sum_remaining += cat['remaining']
        sum_plan += cat['plan']
        
        row = f"""| {(cat['category'].ljust(13)).capitalize()} | {str(cat['spent']).rjust(4)}   {str(cat['plan']).rjust(8)}   {str(cat['remaining']).rjust(8)}
|---------------|----------|----------|----------|"""
        table_rows.append(row)
    
    table_header = "| Категория     | Осталось | Заложено | Потрачено|\n|---------------|----------|----------|----------|"
    
    table_end = f"|------------------------------------------------|\n|  Итог:       | {sum_exp}    | {sum_plan}   | {sum_remaining}   |"
   
    full_table = f"```\n{table_header}\n" + "\n".join(table_rows) + f"\n{table_end}```"
    return full_table