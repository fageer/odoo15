from odoo import models


class BookingXlsx(models.AbstractModel):
    _name = 'report.room_booking.report_booking_details_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, organizers):
        print("=====================XLSX", data['bookings'])

        sheet = workbook.add_worksheet('Bookings')
        bold = workbook.add_format({'bold': True})
        sheet.set_column('A:C', 15)
        sheet.set_column('D:E', 20)
        sheet.set_column('F:G', 25)
        sheet.set_column('H:H', 15)

        row = 0
        col = 0

        sheet.write(row, col, 'Reference', bold)
        sheet.write(row, col+1, 'Room Name', bold)
        sheet.write(row, col+2, 'Room Type', bold)
        sheet.write(row, col+3, 'Organizer', bold)
        sheet.write(row, col+4, 'Booking Status', bold)
        sheet.write(row, col+5, 'From', bold)
        sheet.write(row, col+6, 'To', bold)
        sheet.write(row, col+7, 'Total Of Hours', bold)
        sheet.write(row, col+8, 'Total', bold)
        for booking in data['bookings']:
            row += 1
            sheet.write(row, col, booking['ref'])
            sheet.write(row, col + 1, booking['room_id'][1])
            sheet.write(row, col + 2, booking['room_domain'])
            sheet.write(row, col + 3, booking['organizer'][1])
            sheet.write(row, col + 4, booking['room_state'])
            sheet.write(row, col + 5, booking['start_date'])
            sheet.write(row, col + 6, booking['end_date'])
            sheet.write(row, col + 7, f"{booking['total_of_hours']} hours")
            sheet.write(row, col + 8, f"${booking['total']}")

