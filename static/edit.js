'user strict'


EditarGLC = {
    onLoad:function(){
        $('.add_producao').click( EditarGLC.addProducao );
        $('#save').click( EditarGLC.save );
    },

    addProducao:function(){
        var pai = $(this).parent();
        var clone = $(this).parent().clone();
        var input = $( clone ).find('input').last();
        input.val("");
        $(pai).find('input').last().after("<br/>");
        $(pai).find('button').before(input);
    },

    save:function(){
        var inputs = $('.producao');

        if( inputs.length ){
            var value;
            for( var x=0; x < inputs.length;x++ ){
                value = inputs[x].value;
                var regex = /^([A-Z])\s->\s((\w\s)*((\|\s(\w\s)*)?)*\w\b)/g;
				var test  = value.match(regex);

				if( !test || test[0].length != value.length )
				{
					alert("Regex não é válida.")
                    return false;
				}
                // var test = regex.test(value);
                // if( !test ){
                // }
				// console.log(test);
            }
			$(this).parent().submit();
        }
    }
}
$( document ).ready( EditarGLC.onLoad );
