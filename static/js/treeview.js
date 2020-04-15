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
                  }
                  if(cote.length==3){
                    $.ajax({
                      url:'/repertoire/detail/sousserie/' + cote,
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
                      url:'/repertoire/detail/division/' + cote,
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
                      url:'/repertoire/detail/archive/' + cote,
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
              output += '<a href =" archive/' + result.id +'/detail/">- ' + result.text + '</a>' + '<br>';
            }
            else if(result.tag=='division'){
              output += '<a href ="division/' + result.id +'/detail/">- ' + result.text + '</a>' + '<br>';
            }
            else if(result.tag=='sousserie'){
              output += '<a href ="sousserie/' + result.id +'/detail/">- ' + result.text + '</a>' + '<br>';
            }
            else if(result.tag=='serie'){
              output += '<a href ="serie/' + result.id +'/detail/">- ' + result.text + '</a>' + '<br>';
            }
         });
          $('#search-output').html(output);
        }

        $('#btn-search').on('click',  search );
        $('#input-search').on('keyup', search);
         
      });


      $('#bt-refresh').on('click',function(){
        $.getJSON('/patryarch/repertoire/', function(tree){

            var $tree = $('#repertoire').treeview({
              nodeIcon: "glyphicon glyphicon-folder-close",
              enableLinks: true,
              showTags: true,
              levels: 0,
              data: tree,
              multiSelect: false
            });

        });
      });  
    });



