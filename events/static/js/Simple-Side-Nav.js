$(document).on('click', '.toggle-side-nav', {}, function() {
    if (typeof $(this).data('navId') !== 'undefined')
    {
        let navId = $(this).data('navId');
        $('#'+navId+'.side-nav').toggleClass('open');
    }
    else
    {
        $('.side-nav').toggleClass('open');
    }
});