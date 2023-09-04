/* Contains code the Chapter Page */

/* This creates a offCanvas that has a list that
   links to every verse on the page
*/
function AddSidebar() {

    var number_of_verses = $('#chapter_information').data('n-verses');
    var chapter_no = $('#chapter_information').data('chapter-no');

    var offcanvas_html = `
    <button class="btn btn-lg btn-outline-warning sidebar-button" data-bs-toggle="offcanvas" data-bs-target="#verse_browser_offcanvas" aria-controls="verse_browser_offcanvas">
    <span class="fa fa-lg fa-arrow-right"></span>
    </button>
    <div class="offcanvas offcanvas-start" tabindex="-1" id="verse_browser_offcanvas" aria-labelledby="verse_browser_offcanvas_label">
    <div class="offcanvas-header">
        <h5 class="offcanvas-title" id="verse_browser_offcanvas_label">${chapter_no}. ${chapter_titles_english[chapter_no]}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
    </div>
    <div class="offcanvas-body" id="verse_browser_div">
    </div>
    </div>
    `;

    var content = `<ul class="list-group" id="verse_browser">`
    for (var i = 1; i <= number_of_verses; i++) {
        content += `<a href="#${i}"><li class="list-group-item">${chapter_no}.${i}</li></a>`;
    }
    content += "</ul>";
    $('body').append(offcanvas_html);
    $("#verse_browser_div").append(content);
}

/*
    We disable the default scrollback and have an orange line on top that denotes the scroll position
    It looks much better.
*/

function ProgressBarScrollCallback() {
    let winScroll = document.body.scrollTop || document.documentElement.scrollTop,
        height = document.documentElement.scrollHeight - document.documentElement.clientHeight,
        scrolled = (winScroll / height);

    /* Since we have disabled scroll bars, we will display the scroll position as a line on the top of the page. */
    if (scrolled <= 0) {
        $(".progress-container").fadeOut();
    }
    else {
        $(".progress-container").fadeIn();
        document.getElementById("progressBar").style.width = (scrolled * 100) + "%";
    }
}

/* 
    Open up the share verse link modal.
*/
function ShareVerseLink(modal, selector, chapter, verse)
{
    var domain = location.protocol + '//' + location.host;
    var verseURL = `${domain}/${chapter}.html#${verse}`;
    $(selector).val(verseURL);
    $(modal).modal("show");
}

function CopyVerseLinktoClipboard(selector)
{
    copyTextToClipboard($(selector).val());
}

$(document).ready(() => {
    /* Hide the progress bar */
    $(".progress-container").hide();
    document.addEventListener('scroll', () => {
        ProgressBarScrollCallback();
    });
    AddSidebar();
})