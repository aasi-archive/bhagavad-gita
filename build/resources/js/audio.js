function StopAllAudio()
{
    document.querySelectorAll('audio').forEach(el => el.pause());
}

function PlayAudio(audio_selector)
{
    StopAllAudio();
    audio_element = document.getElementById(audio_selector);
    audio_element.play();
}