/* Creates the chapter cards on index */
function GenerateGitaChapterCard(chapter)
{
    var chapter_card_html = `<div class="col-lg-4 col-md-4 col-sm-12">
    <div class="card shadow-lg my-2">
        <div class="card-body">
            <div class="row">
                <div class="col-3">
                    <a href="/${chapter}.html" class="btn btn-index stretched-link">
                    <img src="/resources/images/index-button.png" width="64px" height="64px"></a>
                </div>
                    <div class="col-9">
                        <div class="chapter-title">
                            <div class="chapter-title-sanskrit">${chapter_titles[chapter]}</div>
                            <div class="chapter-title-english">&nbsp;${chapter_titles_english[chapter]}</div>
                        </div>
                    </div>
            </div>
        </div>
    </div>
    </div>`
    return chapter_card_html;
}

$(document).ready(() => {
    for(var i = 1; i <= 18; i++)
    {
        $("#chapter-cards").append(GenerateGitaChapterCard(i));
    }

    /* For the button that allows us to jump to a verse directly. */
    $('#btn-verse-jumper').click(function () {
        var chapter = $('#chapter-select').val();
        var verse = $('#verse-select').val();
        window.location.href = `/${chapter}.html#${verse}`;
    });

    /* When chapter is changed, change the verses selection panel. */
    $('#chapter-select').on('change', function () {
        var chapter_no = $('#chapter-select').val();
        var max_verses = verses_per_chapter[chapter_no];
        $('#verse-select').html('');
        for(var i = 1; i <= max_verses; i++)
        {
            $('#verse-select').append(`<option value="${i}">${i}</option>`);
        }
    });

    /* Add the 18 chapters */
    for(var i = 1; i <= 18; i++)
    {
        $('#chapter-select').append(`<option value="${i}">${i}. ${chapter_titles[i]}</option>`);
    }
    /* 
        Trigger the chapter-select event on load so that the 47 verses is added to the
        verse selector 
    */
    var chapter_select = document.getElementById('chapter-select');
    chapter_select.dispatchEvent(new Event('change'));
})