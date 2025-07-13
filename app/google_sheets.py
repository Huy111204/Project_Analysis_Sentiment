import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# Thiết lập phạm vi truy cập
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Đường dẫn tới file credentials bạn tải từ Google Cloud Console
SERVICE_ACCOUNT_FILE = "credentials.json"

# ID Google Sheet từ URL của bạn
SPREADSHEET_ID = "11GFPE5lCZZw3zrmzV0dEQw1QBXHszPAECNX52iM6uPg"
SHEET_NAME = "Sheet1"  # hoặc tên khác nếu bạn đổi

def append_feedback_to_gsheet(feedback_dict):
    """feedback_dict là dict gồm các cột: comment, model_prediction, correct_label, timestamp"""
    try:
        # Xác thực và kết nối đến Google Sheets
        creds = Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
        client = gspread.authorize(creds)

        # Mở sheet và lấy worksheet
        sheet = client.open_by_key(SPREADSHEET_ID)
        worksheet = sheet.worksheet(SHEET_NAME)

        # Thêm dữ liệu
        row = [
            feedback_dict.get("comment", ""),
            feedback_dict.get("model_prediction", ""),
            feedback_dict.get("correct_label", ""),
            feedback_dict.get("timestamp", ""),
        ]
        worksheet.append_row(row)
        return True
    except Exception as e:
        print("❌ Gặp lỗi khi ghi vào Google Sheet:", e)
        return False
