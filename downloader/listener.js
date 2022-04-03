(function () {
    var origin = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function () {
        this.addEventListener("load", function () {
            var t = this.responseText;

            if (t.includes(".m3u8") && (t.includes("playlist_") || t.includes("master_dynamic_"))) {
                console.error(t);
            }
        });
        origin.apply(this, arguments);
    };
})();