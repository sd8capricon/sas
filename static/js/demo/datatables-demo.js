// Call the dataTables jQuery plugin

const initTable = (title) => {
  var dtb = $('#dataTable').DataTable();
  if (title == 'tt_test')
    dtb.order([[3, 'asc'], [4, 'asc']]).draw();
}
