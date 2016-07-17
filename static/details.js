'user strict'


ParserGLC = {
    onLoad:function(){
        $('#testar_sentenca').click( ParserGLC.testarSentenca );
    },

    testarSentenca:function(){
		var input = $('#sentenca');
		$.ajax({
			method:"POST",
			url:"",
			data:{"sentenca":input.val()}
		}).done(function( result ){
			var response = result.response;
			$("#result").text(response)
		});
	}
}
$( document ).ready( ParserGLC.onLoad );
