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
})