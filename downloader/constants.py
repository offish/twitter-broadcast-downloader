TIMEOUT = 10

XHR_SCRIPT = """
document.sniffed = '';
(function() {
    var origOpen = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function() {
        console.log('request started!');
        this.addEventListener('load', function() {
            console.log('request completed!');
            console.log(this.readyState); //will always be 4 (ajax is completed successfully)
            console.log(this.responseText);
            document.sniffed += this.responseText;
        });
        origOpen.apply(this, arguments);
    };
})();
"""
GET_SNIFFED_VALUES = "return document.sniffed;"
