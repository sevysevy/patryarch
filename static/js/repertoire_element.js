$(document).ready(function(){

	$('.serie-form').on('click' , function(){
		$.ajax({
		url:'/repertoire/create/serie',
		type:'get',
		datatype:'json',
		beforeSend: function(){
			$('#modal-serie').modal('show');
		},
		success: function(data){
			$('#modal-serie .modal-content').html(data.html_form);
		}
		});
	});

	$('#modal-serie').one('submit', '.create-serie', function(e){
		e.preventDefault();
		var form = $(this);
		$.ajax({
			url : form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType:'json',
			success: function(data){
				
					$('#modal-serie').modal('hide');
					
				}

		});
		return false;
		
	});



	$('.sousserie-form').on('click' , function(){
		$.ajax({
		url:'/repertoire/create/sousserie',
		type:'get',
		datatype:'json',
		beforeSend: function(){
			$('#modal-sousserie').modal('show');
		},
		success: function(data){
			$('#modal-sousserie .modal-content').html(data.html_form);
		}
		});
	});

	$('#modal-sousserie').one('submit','.create_sousserie', function(){
		var form = $(this);
		$.ajax({
			url : form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType:'json',
			success: function(data){	
				$('#modal-sousserie').modal('hide');
				
			}

		})
		return false;
		
	});





	$('.division-form').on('click' , function(){
		$.ajax({
			url:'/repertoire/create/division',
			type:'get',
			datatype:'json',
			beforeSend: function(){
				$('#modal-division').modal('show');
			},
			success: function(data){
				$('#modal-division .modal-content').html(data.html_form);
			}
		});
	});

	$('#modal-division').one('submit', '.create-division', function(){
		e.preventDefault();
		var form = $(this);
		$.ajax({
			url : form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType:'json',
			success: function(data){
				$('#modal-division').modal('hide');
				
			}

		})
		return false;
	});



	$('.archives-form').on('click' , function(){
		$.ajax({
			url:'/repertoire/create/archives',
			type:'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-archives').modal('show');
			},
			success: function(data){
				$('#modal-archives .modal-content').html(data.html_form);
			}
		});
	});

	$('#modal-archives').one('submit', '.create-archive', function(){
		e.preventDefault();
		var form = $(this);
		$.ajax({
			url : form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType:'json',
			success: function(data){
				$('#modal-archives').modal('hide');

			}

		})
		return false;
	});


    $('.btarchives-form').on('click' , function(){
      $.ajax({
         url:'/repertoire/create/boitearchives',
         type:'get',
         datatype:'json',
         beforeSend: function(){
                $('#modal-boitearchives').modal('show');
            },
         success: function(data){
             $('#modal-boitearchives .modal-content').html(data.html);
         }
      });
    });

    $('#modal-boitearchives').one('submit', '.create-boitearchives', function(){
        var form = $(this);
        $.ajax({
            url : form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType:'json',
            success: function(data){
                $('#modal-boitearchives').modal('hide');
            }
        })
        return false;
    });

});