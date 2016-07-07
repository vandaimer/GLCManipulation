'user strict'


AdicionaGLC = {
    onLoad:function(){
        $('.add_producao').click( AdicionaGLC.addProducao );
    },

    addProducao:function(){
        var pai = $(this).parent();
        var clone = $(this).parent().clone();
        var input = $( clone ).find('input').last();
        input.val("");
        $(pai).find('input').last().after("<br/>");
        $(pai).find('button').before(input);
    },

    saveGLC:function(){
        var inputs = $('.nova_producao');
        var producoes = {};

        if( inputs.length ){
            var value;
            for( var x=0; x < inputs.length;x++ ){
                value = inputs[x].value;
                var regex = /^([A-Z])\s->\s((\w\s)*((\|\s(\w\s)*)?)*\w\b)/;
                var test = regex.test(value);
                if( !test ){
                    alert("Regex não é válida.")
                    return false;
                }
                var match = value.match(regex);
                producoes[match[1]] = match[2];
            }
        }
        $.ajax({
            type: "POST",
            url: "add",
            data: JSON.stringify(producoes),
            dataType:"json"
        });
    }
}
$( document ).ready( AdicionaGLC.onLoad );
