import gspread
from google.oauth2.service_account import Credentials

# ======= Cấu hình =======
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "app/credentials.json"  # Lưu ý đường dẫn nếu đặt trong thư mục app/
SPREADSHEET_ID = "11GFPE5lCZZw3zrmzV0dEQw1QBXHszPAECNX52iM6uPg"
SHEET_NAME = "Sentiment Feedback"

def append_feedback_to_gsheet(feedback_dict):
    """
    Ghi một dòng phản hồi vào Google Sheet.
    feedback_dict gồm: comment, model_prediction, correct_label, timestamp
    """
    try:
        # Xác thực credentials
        creds = Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
        client = gspread.authorize(creds)

        # Mở sheet
        sheet = client.open_by_key(SPREADSHEET_ID)
        worksheet = sheet.worksheet(SHEET_NAME)

        # Ghi dữ liệu
        row = [
            feedback_dict.get("comment", ""),
            feedback_dict.get("model_prediction", ""),
            feedback_dict.get("correct_label", ""),
            feedback_dict.get("timestamp", "")
        ]
        worksheet.append_row(row)
        return True

    except Exception as e:
        print(f"❌ Gặp lỗi khi ghi vào Google Sheet: {e}")
        return False
