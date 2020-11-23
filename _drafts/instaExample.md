---
layout: post

---

<script src="javascript/InstagramFeed.min.js"></script>

and then

<!--script>
let feed = new InstagramFeed({
       'username': 'instagram',
            'container': document.getElementById("instagram-feed1"),
            'display_profile': true,
            'display_biography': true,
            'display_gallery': true,
            'callback': null,
            'styling': true,
            'items': 8,
            'items_per_row': 4,
            'margin': 1,
            'lazy_load': true,
            'on_error': console.error
});
</script-->
<script type="text/javascript" src="dist/InstagramFeed.min.js"></script>
<script type="text/javascript">
    (function(){
        new InstagramFeed({
            'username': 'instagram',
            'callback': function(data){
                $('#jsonHere').html(JSON.stringify(data, null, 2));
            }
        });
    })();
</script>
 