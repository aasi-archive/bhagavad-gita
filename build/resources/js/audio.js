/* 
    audio.js - Contains the code for handling the recitation part.
    Working:

    Each verse card in its footer has a <div class="media-player"> 
    containing a play, a stop and an audio button.

    Each audio element has an id, "recitation_<VERSE NO>". Each
    button (.btn-play-audio) and btn-stop-audio has a data called
    "data-audio-pointer" which points to this ID.
*/

// Stop all Audio, pause and then set their times to 0.
function StopAllAudio() {
    document.querySelectorAll('audio').forEach(el => el.pause());
    document.querySelectorAll('audio').forEach(el => el.currentTime = 0);
}

// Play an audio given ID.
function PlayAudio(audio_selector) {
    StopAllAudio();
    audio_element = document.getElementById(audio_selector);
    audio_element.play();
}

// Stop an audio given ID
function StopAudio(audio_selector) {
    audio_element = document.getElementById(audio_selector);
    audio_element.pause();
    audio_element.currentTime = 0;
}

// Add the event listeners
$(document).ready(() => {
    $('.media-player').each(function (i, media_player) {
        // Hide the stop button on init
        $(this).find('.btn-stop-audio').hide();

        // If audio play button is clicked, play the audio
        // and fade in the stop button.
        $(this).find('.btn-play-audio').click(function () {
            PlayAudio($(this).data('audio-pointer'));
            $(media_player).find('.btn-stop-audio').fadeIn();
        });
        
        // Stop button, stop the audio, fade out
        $(this).find('.btn-stop-audio').click(function () {
            StopAudio($(this).data('audio-pointer'));
            $(this).fadeOut();
        });

        // When audio ends, automatically hide the stop button
        $(this).find('audio').on('ended', function () {
            $(media_player).find('.btn-stop-audio').fadeOut();
        });
        
        // Do for pause also
        $(this).find('audio').on('pause', function () {
            $(media_player).find('.btn-stop-audio').fadeOut();
        });
    })
});

