function doGet(e) {
  var sheet = SpreadsheetApp.openById("1K3bKjgQQlUyq1eID8TruBGmejf6co0P2t8ZX99Q1Srk").getActiveSheet();
  var params = e.parameter;
  sheet.appendRow([new Date(), params.sensor_value]);
  return ContentService.createTextOutput("Success");
}
