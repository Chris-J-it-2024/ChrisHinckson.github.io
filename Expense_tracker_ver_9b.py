import json
import os
import time
from datetime import datetime, timedelta
from watchdog.observers import Observer  # Used for monitoring file system changes
from watchdog.events import FileSystemEventHandler  # Handles file system events
import mysql.connector  # MySQL database connector
from mysql.connector import Error  # MySQL error handling
from dotenv import load_dotenv  # Environment variable management
import logging  # For better logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()
def connect_to_database():
        
        """
        Establishes connection to MySQL database using credentials from environment variables.
        Returns:
        mysql.connector.connection: Active database connection or None if connection fails
        Note: Database connection parameters are read from environment variables for security
        """
        
        try:
            connection = mysql.connector.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                database=os.getenv('DB_NAME', 'expense_tracker'),
                user=os.getenv('DB_USER','krys_at_Just_I_T'),
                password=os.getenv('DB_PASSWORD','alnESS625zero?*F')
            )
            if connection.is_connected():
                logging.info("Successfully connected to MySQL database")
                print("Successfully connected to MySQL database")
                return connection
        except Error as e:
            logging.error(f"Error connecting to MySQL database: {e}")
            print(f"Error: {e}")
            return None
print(connect_to_database()        
# class ExpenseTracker:
#     def __init__(self):
#         """
#         Initialize the expense tracker with configuration and connections
#         using 
#         - Sets up file paths from environment variables or defaults
#         - Establishes database connection
#         - Defines valid expense categories
#         - Loads existing expenses from database
#         """
        
#         # Configure file paths from environment variables with fallback defaults
        
#         self.expenses_file = os.getenv('EXPENSES_FILE', 'expenses.json')
#         self.summary_file = os.getenv('SUMMARY_FILE', 'expense_summary.json')
        
#         # Define valid expense categories to ensure data integrity
        
#         self.valid_categories = {'food', 'transport', 'entertainment', 'utilities', 'other'}
        
#         # Establish database connection
        
#         self.db_connection = self.connect_to_database()
        
#         # Load existing expenses into memory
        
#         self.expense_list = []
#         if self.db_connection:
#             self.load_expenses()

#     def connect_to_database(self):
        
#         """
#         Establishes connection to MySQL database using credentials from environment variables.
#         Returns:
#         mysql.connector.connection: Active database connection or None if connection fails
#         Note: Database connection parameters are read from environment variables for security
#         """
        
#         try:
#             connection = mysql.connector.connect(
#                 host=os.getenv('DB_HOST', 'localhost'),
#                 database=os.getenv('DB_NAME', 'expense_tracker'),
#                 user=os.getenv('DB_USER'),
#                 password=os.getenv('DB_PASSWORD')
#             )
#             if connection.is_connected():
#                 logging.info("Successfully connected to MySQL database")
#                 return connection
#         except Error as e:
#             logging.error(f"Error connecting to MySQL database: {e}")
#             return None

#     def load_expenses(self):
#         """
#         Loads all expenses from database into memory.
#         """
#         if self.db_connection:
#             try:
#                 cursor = self.db_connection.cursor(dictionary=True)
#                 cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
#                 self.expense_list = cursor.fetchall()
#             except Error as e:
#                 logging.error(f"Error loading expenses: {e}")
#             finally:
#                 cursor.close()

#     def save_expense(self, expense_data):
#         """
#         Saves a new expense record to the database.
#         """
#         if self.db_connection:
#             try:
#                 cursor = self.db_connection.cursor()
#                 query = """INSERT INTO expenses 
#                         (user_id, category_id, amount, description, date) 
#                         VALUES (%s, (SELECT category_id FROM categories WHERE name = %s), %s, %s, %s)"""
#                 values = (
#                     expense_data['user_id'],
#                     expense_data['category'],
#                     expense_data['amount'],
#                     expense_data['description'],
#                     expense_data['date']
#                 )
#                 self.db_connection.start_transaction()
#                 cursor.execute(query, values)
#                 self.db_connection.commit()
#                 logging.info("Expense saved successfully")
#                 return True
#             except Error as e:
#                 self.db_connection.rollback()
#                 logging.error(f"Error saving expense: {e}")
#                 return False
#             finally:
#                 cursor.close()
#         return False

#     def archive_old_expenses(self, archive_date):
#         """
#         Archives expenses older than a specified date.
#         """
#         if self.db_connection:
#             try:
#                 cursor = self.db_connection.cursor()
#                 self.db_connection.start_transaction()

#                 # Archive old records
#                 archive_query = """
#                 INSERT INTO archived_expenses (user_id, category_id, amount, description, date)
#                 SELECT user_id, category_id, amount, description, date 
#                 FROM expenses 
#                 WHERE date < %s
#                 """
#                 cursor.execute(archive_query, (archive_date,))

#                 # Delete archived records from main table
#                 delete_query = "DELETE FROM expenses WHERE date < %s"
#                 cursor.execute(delete_query, (archive_date,))

#                 self.db_connection.commit()
#                 logging.info(f"Archived and deleted expenses older than {archive_date}")
#             except Error as e:
#                 self.db_connection.rollback()
#                 logging.error(f"Error archiving expenses: {e}")
#             finally:
#                 cursor.close()

#     def validate_expense(self, expense_data):
#         """
#         Validates expense data before saving.
#         """
#         REQUIRED_FIELDS = {'user_id', 'category', 'amount', 'description', 'date'}
#         missing_fields = REQUIRED_FIELDS - expense_data.keys()
#         if missing_fields:
#             return False, f"Missing required fields: {', '.join(missing_fields)}"
        
#         if not isinstance(expense_data['amount'], (int, float)) or expense_data['amount'] <= 0:
#             return False, "Amount must be a positive number"

#         if expense_data['category'] not in self.valid_categories:
#             return False, "Invalid category"

#         if not expense_data['description'].strip():
#             return False, "Description cannot be empty"

#         return True, ""

#     def update_summary(self):
#         """
#         Updates summary file with current expense data.
#         """
#         summary_data = self.calculate_summary()
#         if summary_data:
#             try:
#                 with open(self.summary_file, 'w') as file:
#                     json.dump(summary_data, file, indent=2)
#                 logging.info("Summary file updated successfully")
#             except OSError as e:
#                 logging.error(f"Error writing summary file: {e}")

# class NewExpenseHandler(FileSystemEventHandler):
#     """
#     Handles file system events for new expense submissions.
#     """
#     def __init__(self, expense_tracker):
#         self.expense_tracker = expense_tracker

#     def on_created(self, event):
#         if event.src_path.endswith('.json'):
#             try:
#                 time.sleep(0.1)  # Ensure the file is fully written
#                 with open(event.src_path, 'r') as file:
#                     expense_data = json.load(file)
#                 valid, message = self.expense_tracker.validate_expense(expense_data)
#                 if valid:
#                     self.expense_tracker.save_expense(expense_data)
#                 else:
#                     logging.warning(f"Invalid expense data: {message}")
#                 os.remove(event.src_path)  # Remove processed file
#             except Exception as error:
#                 logging.error(f"Error processing new expense: {error}")

# def main():
#     """
#     Main function to run the expense tracker.
#     """
#     tracker = ExpenseTracker()
#     archive_threshold = datetime.now() - timedelta(days=365)
#     tracker.archive_old_expenses(archive_threshold)

#     event_handler = NewExpenseHandler(tracker)
#     file_observer = Observer()
#     file_observer.schedule(event_handler, path='.', recursive=False)
#     file_observer.start()

#     logging.info("Expense tracker is running. Press Ctrl+C to exit.")
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         file_observer.stop()
#         if tracker.db_connection:
#             tracker.db_connection.close()
#     file_observer.join()

# if __name__ == "__main__":
#     main()
