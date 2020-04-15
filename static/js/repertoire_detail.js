$(document).ready(function(){
	$('.treeview').delegate('.list-group-item','click', function(){
        var info = $(this).text()
		var index_endcote = info.indexOf(" ")
		var cote = info.substr(0,index_endcote)

		$.ajax({
			url:'/repertoire/detail/serie/' + cote,
			type:'get',
			datatype:'json',
			beforeSend: function(){
				$('#modal-detailserie').modal('show');
			},
			success: function(data){
				$('#modal-detailserie .modal-content').html(data.html);
			}
		});

    }); 

});