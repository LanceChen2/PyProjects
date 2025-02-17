from openpyxl import load_workbook, Workbook

wb = load_workbook(f"C:\\Users\\user\\OneDrive\\桌面\\test.xlsx")

ws = wb['Sheet1']

ws_props = ws.sheet_properties
ws.auto_filter.ref = ws.dimensions
ws.auto_filter.add_filter_column(1, [])

wb.save(f"C:\\Users\\user\\OneDrive\\桌面\\test1.xlsx")