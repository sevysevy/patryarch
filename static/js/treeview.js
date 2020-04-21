$(document).ready( function() {
  $.getJSON('/repertoire/tree_views/', function(tree){
    var $tree = $('#repertoire').treeview({
      nodeIcon: "glyphicon glyphicon-folder-close",
      enableLinks: false,
      showTags: true,
      levels: 0,
      data: tree,
      multiSelect: false
    })

  $('.treeview').on('nodeSelected', function(event, data) {
    var info = data.text
    var index_endcote = info.indexOf(" ")
    var cote = info.substr(0,index_endcote)
    if(cote.length==1){
      $.ajax({
        url:'/repertoire/serie/' + cote + '/detail',
        type:'get',
        datatype:'json',
        beforeSend: function(){
          $('#modal-detailserie').modal('show');
        },
        success: function(data){
          $('#modal-detailserie .modal-content').html(data.html);
        }
      });
    }
    if(cote.length==3){
      $.ajax({
        url:'/repertoire/sousserie/' + cote + '/detail',
        type:'get',
        datatype:'json',
        beforeSend: function(){
          $('#modal-detailsserie').modal('show');
        },
        success: function(data){
          $('#modal-detailsserie .modal-content').html(data.html);
        }
      });
    }    
    if(cote.length==7){
      $.ajax({
        url:'/repertoire/division/' + cote + '/detail',
        type:'get',
        datatype:'json',
        beforeSend: function(){
          $('#modal-detaildivision').modal('show');
        },
        success: function(data){
          $('#modal-detaildivision .modal-content').html(data.html);
        }
      });
    }   
    if(cote.length==11){
      $.ajax({
        url:'/repertoire/archive/' + cote + '/detail',
        type:'get',
        datatype:'json',
        beforeSend: function(){
          $('#modal-detailarchive').modal('show');
        },
        success: function(data){
          $('#modal-detailarchive .modal-content').html(data.html);
        }
      });
    }                             
  });

              
          var search = function(e) {
            var pattern = $('#input-search').val();
            var options = {
            ignoreCase: true,
            exactMatch: false,
            revealResults: true
            };
           

           var results = $tree.treeview('search', [ pattern, options ]);
           var output = '<p>' + results.length + ' resultats trouvés</p>';
           $.each(results, function (index, result) {
            
            if(result.tag=='archive'){
              output +=  result.text + '<br>';
            }
            else if(result.tag=='division'){
              output += result.text +  '<br>';
            }
            else if(result.tag=='sousserie'){
              output +=  result.text +  '<br>';
            }
            else if(result.tag=='serie'){
              output += result.text +  '<br>';
            }
         });
          $('#search-output').html(output);
        }

        $('#btn-search').on('click',  search );
        $('#input-search').on('keyup', search);
         
      });


      $('#bt-refresh').on('click',function(){
        $.getJSON('/repertoire/tree_views/', function(tree){

            var $tree = $('#repertoire').treeview({
              nodeIcon: "glyphicon glyphicon-folder-close",
              showTags: true,
              levels: 0,
              data: tree,
              multiSelect: false
            });

            $('.treeview').on('nodeSelected', function(event, data) {
          var info = data.text
          var index_endcote = info.indexOf(" ")
          var cote = info.substr(0,index_endcote)
          if(cote.length==1){
            $.ajax({
              url:'/repertoire/serie/' + cote + '/detail',
              type:'get',
              datatype:'json',
              beforeSend: function(){
                $('#modal-detailserie').modal('show');
              },
              success: function(data){
                $('#modal-detailserie .modal-content').html(data.html);
              }
            });
          }
          if(cote.length==3){
            $.ajax({
              url:'/repertoire/sousserie/' + cote + '/detail',
              type:'get',
              datatype:'json',
              beforeSend: function(){
                $('#modal-detailsserie').modal('show');
              },
              success: function(data){
                $('#modal-detailsserie .modal-content').html(data.html);
              }
            });
          }    
          if(cote.length==7){
            $.ajax({
              url:'/repertoire/division/' + cote + '/detail',
              type:'get',
              datatype:'json',
              beforeSend: function(){
                $('#modal-detaildivision').modal('show');
              },
              success: function(data){
                $('#modal-detaildivision .modal-content').html(data.html);
              }
            });
          }   
          if(cote.length==11){
            $.ajax({
              url:'/repertoire/archive/' + cote + '/detail',
              type:'get',
              datatype:'json',
              beforeSend: function(){
                $('#modal-detailarchive').modal('show');
              },
              success: function(data){
                $('#modal-detailarchive .modal-content').html(data.html);
              }
            });
          }                             
        });
        });
        
      });  
    });



