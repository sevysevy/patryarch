$(document).ready( function() {
      $.getJSON('/repertoire/tree_views/', function(tree){
            var $tree = $('#repertoire').treeview({
              nodeIcon: "glyphicon glyphicon-folder-close",
              enableLinks: true,
              showTags: true,
              levels: 0,
             data: tree,
             multiSelect: false
            })
             $('.treeview').delegate('.list-group-item','hover', function(){
                   $(this).css('background-color','#fbf');
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