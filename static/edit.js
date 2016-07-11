'user strict'


EditarGLC = {
    onLoad:function(){
        $('.add_producao').click( EditarGLC.addProducao );
        $('#save').click( EditarGLC.save );
    },

    addProducao:function(){
        var input = $( 'form' ).find('input').last().clone();
        input.val("");
        $('form').find('fieldset').append(input)
    },

    save:function(){
        var inputs = $('.producao');
        var toRemoval = []

        if( inputs.length ){
            var value;
            for( var x=0; x < inputs.length;x++ ){
                value = inputs[x].value;
                if( value === "" ){
                    toRemoval.push(inputs[x]);
                } else {
                    var regex = /^([A-Z])\s->\s((\w\s)*((\|\s(\w\s)*)?)*\w\b)/g;
                    var test  = value.match(regex);

                    if( !test || test[0].length != value.length )
                    {
                        alert("Produção inválida.")
                        return false;
                    }
                }
            }
            toRemoval.forEach(function(item){
                $(item).remove();
            });
            $('form').submit();
        }
    }
}
$( document ).ready( EditarGLC.onLoad );
