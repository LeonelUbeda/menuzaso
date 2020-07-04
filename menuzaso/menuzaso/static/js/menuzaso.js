$( document ).ready(function(){
    
    rotateClass = 'arrow-rotate'
    $('.dish').click(function(){
        console.log('Hol')
        if($(window).width() < 425){
            arrow = $(this).find('.arrow')
            if(arrow.hasClass(rotateClass)){
                arrow.removeClass(rotateClass)

            }else{
                arrow.addClass(rotateClass)

            }
            $(this).find('.ingredients.mobile-425').slideToggle(400)
        }

    })

    $(window).resize(function (){
        if($(window).width() > 425){
            arrow = $(this).find('.arrow')
            arrow.removeClass(rotateClass)
            $('.mobile-425').css('display', 'none')
        }else{
            $('.arrow.mobile-425').css('display', 'block')
        }
    })
})