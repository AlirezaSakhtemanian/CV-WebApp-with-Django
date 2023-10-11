$('.progress-bar').each(function () {
    var value = $(this).attr('aria-valuenow');
    $(this).css('width', value + '%');
});

function fillParentId(parentId) {
    $('#id_parent').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}

var currentUrl = window.location.href;
if (currentUrl.indexOf('/fa/') !== -1) {
    $("body").addClass('font-persian');
} else {
    $("body").removeClass('font-persian');
}

function goingBack() {
    window.history.back();
}

hljs.highlightAll();
hljs.initLineNumbersOnLoad();
hljs.addPlugin(new CopyButtonPlugin());

$(function () {
    var top = $('#header-blog').height();
    $(window).scroll(function (evt) {
        var y = $(this).scrollTop();
        if (y > top) {
            $('#sidebar').addClass('fixed');
        } else {
            $('#sidebar').removeClass('fixed');
        }
    });
});

// $('.sidebar-link').click(function () {
//     var target = $(this).attr('href');
//     var position = $(target).position().top - 100;
//     $('html, body').animate({
//         scrollTop: position
//     }, 500);
// })