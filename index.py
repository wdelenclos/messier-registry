index = """
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<meta name="description" content="Entrepreneur, Développeur et UX Designer. Vous cherchez à en savoir plus sur moi, c'est ici.">
<meta name="author" content="Wladimir Delenclos">
<meta name="theme-color" content="#222526">
<title>Space object registry</title>
<style>
        body {
            background: linear-gradient(180deg, #2E2F31 0%, #222526 51.04%, #1b1e1f 100%);
            min-height: 100vh;
            background-repeat: no-repeat;
            font-family: 'DM Sans', sans-serif;
            color: #fff
        }
        .content{
            padding: 3em
        }
        h1{
            font-weight: 400;
            font-size: 1em;
            margin-bottom: 3em;
        }
        h1 > span{
            color: #74757a;
        }
        .sec{
            font-size: 0.7em;
        }
        .card{
            background: linear-gradient(180deg, rgba(76, 79, 80, 0.31) 0%, rgba(50, 52, 53, 0.4) 100%);
            border: 1px solid #3F4041;
            font-size: 1.1em;
            border-radius: 10px;
            margin-bottom: 1em;
            box-shadow: 0px 40px 60px rgba(23, 24, 24, 0.34);
        }
        .card-header{
            background: rgba(63, 63, 64, 0.3);
            height: 42px;
            border-radius: 10px 10px 0 0;
            line-height: 42px;
            padding-left: 1.8em;
            font-size: 0.8em;
            color: #87888e;
        }
        .card-body{
            padding: 0.8em 2em
        }
        h2{
            font-size: 1.4em;
            margin-bottom: 0.3em;
            font-weight: 400;
        }
        p{
            font-size: 0.95em;
            color: #eaeaea;
            line-height: 1.5;
            font-weight: 400;
        }
        .hour{
            float: right;
        }
        /*  SECTIONS  */
        .section {
            clear: both;
            padding: 0px;
            margin: 0px;
        }
        .card-article-list{
            padding: 1em 0;
        }
        .card-article-list > ul{
            list-style-type: none;
            padding: 0 2em;
        }
        .small{
            font-size: 0.95em;
        }
        .card-article-list > ul > a  {
            color: #ffffff!important;
            text-decoration: none;
            font-size: 1em;
            line-height: 1.8em;
        }
        .card-article-list > ul > a > li{
            transition-duration: .2s;
            width: 100%;
            margin-bottom: 0.5em;
            padding-bottom: 0.5em;
            border-bottom: solid 1px rgba(255, 255, 255, 0.11);
        }
        .card-article-list > ul > a > li:hover{
           border-color: rgba(255, 255, 255, 0.46);
        }
        .card-article{}
        /*  COLUMN SETUP  */
        .col {
            display: block;
            float:left;
            margin: 1% 0 1% 1.6%;
        }
        .col:first-child { margin-left: 0; }


        /*  GROUPING  */
        .group:before,
        .group:after {
            content:"";
            display:table;
        }
        .group:after {
            clear:both;
        }
        .group {
            zoom:1; /* For IE 6/7 */
        }

        /*  GRID OF THREE  */
        .span_3_of_3 {
            width: 100%;
        }
        .span_2_of_3 {
            width: 66.1%;
        }
        .span_1_of_3 {
            width: 32.2%;
        }

        /*  GO FULL WIDTH AT LESS THAN 480 PIXELS */

        @media only screen and (max-width: 920px) {
            html{
                font-size: 13px;
            }
            .content{
                padding: 1em;
            }
            .col { margin: 1% 0 1% 0%;}
            .span_3_of_3, .span_2_of_3, .span_1_of_3 { width: 100%; }
        }
    </style>
</head>
<body>
<div class="content">
<h1>Space Object Registry <span> The scientific messier's articles database</span></h1>
<div class="section group">
<div class="col span_2_of_3">
<section class="card">
<div class="card-header">
<span>Bienvenue</span>
</div>
<div class="card-body">
<h2>Introduction</h2>
<p>Space Object Registry is an article database for messier objects. Discover every scientific articles availables about space objects.</p>
<a style="color: #fff; margin-bottom: 24px; display: inline-block" href="https://github.com/wdelenclos/messier-registry">See documentation</a>
</div>
</section>
</div>
<div class="col span_1_of_3">
<section class="card">
<div class="card-header">
<span>Info about API</span>
</div>
<div class="card-body">
<h2 id="status">Online</h2>
<p>Version: 1.0</p>
</div>
</section>
</div>
</div>
</div>
</body>
<script>
    function getAPIStatus(){
        if (window.fetch) {
            fetch('http://space.wdelenclos.fr/api/v1')
                .then(
                    function(response) {
                    if (response.status !== 200) {
                        console.log('Looks like there was a problem. Status Code: ' +
                        response.status);
                        return;
                    }

                    // Examine the text in the response
                    response.json().then(function(data) {
                        console.log(data.status);
                    });
                    }
                )
                .catch(function(err) {
                    console.log('Fetch Error :-S', err);
                });
        } else {
            
        }
    }
    function getObj(){
        if (window.fetch) {
            fetch('http://space.wdelenclos.fr/api/v1/objects')
                .then(
                    function(response) {
                    if (response.status !== 200) {
                        console.log('Looks like there was a problem. Status Code: ' +
                        response.status);
                        return;
                    }

                    // Examine the text in the response
                    response.json().then(function(data) {
                        console.log(data.length);
                    });
                    }
                )
                .catch(function(err) {
                    console.log('Fetch Error :-S', err);
                });
        } else {
            
        }
    }
    getAPIStatus();
    getObj();
</script>
</html>
"""