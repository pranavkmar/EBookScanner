/*!
 * IE10 viewport hack for Surface/desktop Windows 8 bug
 * Copyright 2014-2015 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */

// See the Getting Started docs for more information:
// http://getbootstrap.com/getting-started/#support-ie10-width

(function () {
  'use strict';

  if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
    var msViewportStyle = document.createElement('style')
    msViewportStyle.appendChild(
      document.createTextNode(
        '@-ms-viewport{width:auto!important}'
      )
    )
    document.querySelector('head').appendChild(msViewportStyle)
  }

})();

var sizes = {
 "240p" : [320, 240],
 "480p" : [640, 480],
 "720p" : [960, 720],
 "FHD 720p" : [1280, 720],
 "FHD 1080p" : [1920, 1080],
};
var cursz = (typeof(Storage) !== "undefined" && localStorage.cursz && sizes[localStorage.cursz]) ? localStorage.cursz : ((window.screen.width < 640) ? "240p" : "480p");
