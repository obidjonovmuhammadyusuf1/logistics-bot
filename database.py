import aiosqlite
import asyncio

DB_NAME = "expenses.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                amount REAL,
                currency TEXT,
                category TEXT,
                description TEXT,
                date TEXT
            )
        ''')
        await db.commit()

async def add_expense(user_id, amount, currency, category, description):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO expenses (user_id, amount, currency, category, description, date) VALUES (?, ?, ?, ?, ?, datetime('now'))",
            (user_id, amount, currency, category, description)
        )
        await db.commit()

async def get_today_expenses(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT currency, SUM(amount) as total FROM expenses WHERE user_id = ? AND date(date) = date('now') GROUP BY currency",
            (user_id,)
        )
        return await cursor.fetchall()