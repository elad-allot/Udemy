from bs4 import BeautifulSoup

SIMPLE_HTML = '''
<html lang="en"><head><script type="text/javascript">

(function() {
	if(typeof amzn_assoc_utils==="undefined"){amzn_assoc_utils={};}if(typeof amzn_assoc_utils.parse==="undefined"){amzn_assoc_utils.parse=(function(){var d,b,a={'"':'"',"\\":"\\","/":"/",b:"\b",f:"\f",n:"\n",r:"\r",t:"\t"},m,k=function(n){throw {name:"SyntaxError",message:n,at:d,text:m};},g=function(n){if(n&&n!==b){k("Expected '"+n+"' instead of '"+b+"'");}b=m.charAt(d);d+=1;return b;},f=function(){var o,n="";if(b==="-"){n="-";g("-");}while(b>="0"&&b<="9"){n+=b;g();}if(b==="."){n+=".";while(g()&&b>="0"&&b<="9"){n+=b;}}if(b==="e"||b==="E"){n+=b;g();if(b==="-"||b==="+"){n+=b;g();}while(b>="0"&&b<="9"){n+=b;g();}}o=+n;if(!isFinite(o)){k("Bad number");}else{return o;}},h=function(){var q,p,o="",n;if(b==='"'){while(g()){if(b==='"'){g();return o;}if(b==="\\"){g();if(b==="u"){n=0;for(p=0;p<4;p+=1){q=parseInt(g(),16);if(!isFinite(q)){break;}n=n*16+q;}o+=String.fromCharCode(n);}else{if(typeof a[b]==="string"){o+=a[b];}else{break;}}}else{o+=b;}}}k("Bad string");},j=function(){while(b&&b<=" "){g();}},c=function(){switch(b){case"t":g("t");g("r");g("u");g("e");return true;case"f":g("f");g("a");g("l");g("s");g("e");return false;case"n":g("n");g("u");g("l");g("l");return null;}k("Unexpected '"+b+"'");},l,i=function(){var n=[];if(b==="["){g("[");j();if(b==="]"){g("]");return n;}while(b){n.push(l());j();if(b==="]"){g("]");return n;}g(",");j();}}k("Bad array");},e=function(){var o,n={};if(b==="{"){g("{");j();if(b==="}"){g("}");return n;}while(b){o=h();j();g(":");if(Object.hasOwnProperty.call(n,o)){k('Duplicate key "'+o+'"');}n[o]=l();j();if(b==="}"){g("}");return n;}g(",");j();}}k("Bad object");};l=function(){j();switch(b){case"{":return e();case"[":return i();case'"':return h();case"-":return f();default:return b>="0"&&b<="9"?f():c();}};return function(p,o){var n;m=p;d=0;b=" ";n=l();j();if(b){k("Syntax error");}return n;};}());}if(typeof amzn_assoc_utils.stringify==="undefined"){amzn_assoc_utils.stringify=function(b){var a="";if(typeof JSON!=="undefined"){a=JSON.stringify(b);}return a;};}if(typeof amzn_assoc_utils.addCssRules==="undefined"){amzn_assoc_utils.addCssRules=function(g,n){var h=document.createElement("style"),m,e=0,k="";h.appendChild(document.createTextNode(""));document.head.appendChild(h);m=h.sheet;for(e=0,rl=n.length;e<rl;e++){var d=1,l=n[e],b=n[e][0],f="";if(Object.prototype.toString.call(l[1][0])==="[object Array]"){l=l[1];d=0;}for(var c=l.length;d<c;d++){var a=l[d];f+=a[0]+":"+a[1]+(a[2]?" !important":"")+";\n";}if(typeof g==="string"){m.insertRule(g+"{"+b+"{"+f+"}}",m.cssRules.length);}else{m.insertRule(b+"{"+f+"}",m.cssRules.length);}}};}window.trackingUtils=function(l,c,e,o,p,h,d,r,t,n,q){var g={},j=new RegExp("/(ref=[\\w]+)/?","i"),a="assocPayloadId",i=function(u){return u&&encodeURIComponent(u).replace(/&/g,"&amp;").replace(/"/g,"&quot;").replace(/</g,"&lt;").replace(/>/g,"&gt;");},m=(function(){var u=document.createElement("a");u.href=(window.location!==window.parent.location)?document.referrer:document.location;return u.protocol+"//"+u.hostname+((u.port===""||u.port==="80"||u.port==="443")?"":(":"+u.port))+(u.pathname.indexOf("/")!==0?("/"+u.pathname):u.pathname);}()),s=(function(){return i(m);}()),k=function(u,w,x,v){if(typeof x==="string"&&x!==""){if(u.search===""){u.search="?"+w+"="+x;}else{if(!u.search.match(new RegExp("[?&]"+w+"="))){u.search=u.search.replace(/\?/,"?"+w+"="+x+"&");}else{if(v){u.search=u.search.replace(new RegExp(w+"=([^&]*)"),w+"="+x);}}}}return u;},f=function(w,u,v){if(typeof v==="string"&&v!==""){if(!w.match(/\?/)){w=w+"?"+u+"="+v;}else{if(!w.match(u)){w=w.replace(/\?/,"?"+u+"="+v+"&");}}}return w;},b=function(v){var u=(typeof d!=="undefined")?d:0;if(typeof v!=="undefined"){u=v;}return u;};g.addRefUrls=function(z,A,v,u){var B=new RegExp("^http://.*(amazon|endless|myhabit|amazonwireless|javari|smallparts)\\.(com|ca|co\\.jp|de|fr|co\\.uk|cn|it|es)/.*","i"),w,y,x;for(x=0;x<z.length;x++){z[x].rel="nofollow";w=String(z[x].href);if(y=w.match(B)){z[x].href=g.addTrackingParameters(z[x],A,v,u);}}};g.addRefRefUrl=function(u){return k(u,"ref-refURL",s);};g.getRefRefUrl=function(){return s;};g.getRawRefUrl=function(){return m;};g.addSignature=function(v,u,w){return k(k(v,"sig",u),"sigts",w);};g.addLinkCode=function(v,u){return k(v,"linkCode",u);};g.addTrackingId=function(v,u){return k(v,"tag",u);};g.addLinkId=function(u,v){return k(u,"linkId",v);};g.addSubtag=function(u,v){return k(u,"ascsubtag",v);};g.addCreativeAsin=function(u,v){return k(k(u,"creativeASIN",v),"adId",v);};g.addAdType=function(v,u){return k(v,"adType",u);};g.addAdMode=function(u,v){return k(u,"adMode",v);};g.addAdFormat=function(v,u){return k(v,"adFormat",u);};g.addImpressionTimestamp=function(u,v){if(typeof v==="number"){v=v.toString();}return k(u,"impressionTimestamp",v);};g.convertToRedirectedUrl=function(u,x,v){var w=document.createElement("a");w.setAttribute("href",x);if(typeof v!=="undefined"){k(w,v,i(u.getAttribute("href")),true);}else{w.setAttribute("href",x+"/"+w.getAttribute("href"));}u.setAttribute("href",w.getAttribute("href"));return u;};g.getImpressionToken=function(){return h;};g.generateTransitId=function(){return g.getHashedImpressionToken();};g.getHashedImpressionToken=function(){var u=o.split("/");var v=u[u.length-2];return v;};g.getTransitId=function(){if(typeof assoc_session_storage!=="undefined"){var u=assoc_session_storage.get(a);return u;}return null;};g.getClickUrl=function(){return p;};g.addImpressionToken=function(v,w){var u=b(w);if(typeof h==="string"&&h!==""){k(v,"imprToken",h);if(typeof u!=="undefined"){k(v,"slotNum",u);}}return v;};g.addImpressionTokenStr=function(w,v){var u=b(v);if(typeof h==="string"&&h!==""){w=f(w,"imprToken",h);if(typeof u!=="undefined"){w=f(w,"slotNum",u);}}return w;};g.addTrackingParameters=function(A,B,z,E,x,u,y,w,v,F,D,C){return g.addSignature(g.addCreativeAsin(g.addLinkId(g.addTrackingId(g.addSubtag(g.addLinkCode(g.addRefRefUrl(g.addImpressionToken(g.addRefMarker(g.addAdType(g.addAdMode(g.addAdFormat(g.addImpressionTimestamp(A,C),D),F),v),x))),z),r),E),B),u),y,w);};g.addRefMarker=function(v,x){var w,u=false;if(typeof x==="undefined"){return v;}if(w=v.pathname.match(j)){v.pathname=v.pathname.replace(w[1],"ref="+x);}else{u=(v.pathname.charAt(v.pathname.length-1)==="/");v.pathname=v.pathname+(u?"":"/")+"ref="+x;}return v;};g.getRefMarker=function(u){var v;if(v=u.pathname.match(j)){return v[1].substr(4);}else{return undefined;}};g.getCurrentURL=function(){return(window.location!==window.parent.location)?document.referrer:document.location.href;};g.makeForesterCall=function(w){var u=undefined,v;if(typeof JSON!=="undefined"){v=JSON.stringify(w);}else{if(typeof amzn_assoc_utils!=="undefined"&&typeof amzn_assoc_utils.stringify==="function"){v=amzn_assoc_utils.stringify(w);}else{return;}}if(typeof o==="string"){u=o+"?assoc_payload="+encodeURIComponent(v);g.generateImage(u);}};g.recordImpression=function(w,u,z,x,B){z.linkCode=w;z.trackingId=u;z.refUrl=g.getCurrentURL();if(n||!t){g.makeForesterCall(z);}else{g.addABPFlag(z,g.makeForesterCall);}if(typeof x==="undefined"||!x){var y=(new Date()).getTime();var A=(typeof B!=="undefined")?B:"";var v=e+"?l="+w+"&t="+u+"&o="+l+"&cb="+y+A;g.generateImage(v);}};g.createAssocPayload=function(y,w,v,u){y.linkCode=w;y.trackingId=v;y.refUrl=u;var x="";if(typeof amzn_assoc_utils!=="undefined"&&typeof amzn_assoc_utils.stringify==="function"){x=amzn_assoc_utils.stringify(y);}return x;};g.recordAESImpression=function(w,u,x){if(typeof q==="string"){var z=g.createAssocPayload(x,w,u,g.getCurrentURL());var v=g.getHashedImpressionToken();var y=q+v+"/pixel?assoc_payload="+encodeURIComponent(z);g.generateImage(y);}};g.recordTransit=function(){if(!(g.getTransitId())||g.isUTMParamPresentInUrl(g.getCurrentURL())){assoc_session_storage.set(a,g.generateTransitId());}};g.isUTMParamPresentInUrl=function(v){var u=v.match(/utm_source=/i);return(u!==null);};g.addAAXClickUrls=function(v){var x,w,u;if(typeof v==="undefined"||typeof p==="undefined"){return;}for(w=0;w<v.length;w++){u=String(v[w].href);if(u.indexOf(p)<0){x=p+u;v[w].href=x;}}};g.addAAXClickUrl=function(u){if(typeof u==="undefined"||u.indexOf(p)===0){return u;}return p+u;};g.updateLinks=function(v,x){var w,u;if(typeof x!=="function"){return;}for(w=0;w<v.length;w++){u=String(v[w].href);v[w].href=x(u);}};g.elementInViewPort=function(u){var v=u.getBoundingClientRect(),w=(v.top>=0&&v.left>=0&&v.bottom<=(window.innerHeight||document.documentElement.clientHeight)&&v.right<=(window.innerWidth||document.documentElement.clientWidth));return{posX:v.left+window.pageXOffset,posY:v.top+window.pageYOffset,inViewPort:w};};g.recordViewability=function(z,y,v,w){if(typeof o==="string"){var x=g.createViewbilityPayload(z,y,v,w);var u=o+x+"&cb="+(new Date()).getTime();g.generateImage(u);}};g.recordAESViewability=function(B,A,v,w){if(typeof q==="string"){var x=g.createViewbilityPayload(B,A,v,w);var u=g.getHashedImpressionToken();var z=encodeURIComponent(x);var y=q+u+"/pixel/"+z+"&cb="+(new Date()).getTime();g.generateImage(y);}};g.createViewbilityPayload=function(z,y,v,x){var w={};if(typeof y!=="undefined"){w.above_the_fold=y;}if(typeof v!=="undefined"){w.topPos=v;}if(typeof x!=="undefined"){w.leftPos=x;}if(typeof z!=="undefined"){if(Object.keys(w).length===0){w.viewable=true;}w.slotNum=z;}var u="";if(typeof amzn_assoc_utils!=="undefined"&&typeof amzn_assoc_utils.stringify==="function"){u=amzn_assoc_utils.stringify({adViewability:[w]});}return u;};g.generateImage=function(u){if(typeof u!=="undefined"){(new Image()).src=u;}};g.addABPFlag=function(x,F){var z=false,y=2,w=document.body?document.body.appendChild(new Image()):new Image(),v=document.body?document.body.appendChild(new Image()):new Image(),C=false,A=false,u=Math.random()*11,E=t+"?ch=*&rn=*",D=function(H,G){if(y===0||G>1000){x.supplySideMetadata={ABPInstalled:y===0&&z};H(x);}else{setTimeout(function(){D(H,G*2);},G*2);}},B=function(){if(--y){return;}z=!C&&A;};w.style.display="none";v.style.display="none";w.onload=B;w.onerror=function(){C=true;B();};w.src=E.replace(/\*/,1).replace(/\*/,u);v.onload=B;v.onerror=function(){A=true;B();};v.src=E.replace(/\*/,2).replace(/\*/,u);D(F,250);};return g;};var assoc_session_storage=(function(){var a={};a.get=function(c){var d=null;if(typeof(window.sessionStorage)!=="undefined"){try{d=window.sessionStorage.getItem(c);}catch(b){}}return d;};a.set=function(c,d){if(typeof(window.sessionStorage)!=="undefined"){try{window.sessionStorage.setItem(c,d);}catch(b){}}};return a;}());window.elemTracker=function(b){var a={};a.trackElements=function(d,c){var f,e;if(typeof d!=="undefined"&&d.length>0&&typeof c==="function"){window.addEventListener("scroll",function(){for(f=0;f<d.length;f++){e=b.elementInViewPort(d[f]);if(e.inViewPort){c();}}},false);}};return a;};
	var amznAutoTaggerMaker=function(h,v,B){var D={CA:"ca",CN:"cn",IN:"in",DE:"de",FR:"fr",GB:"co.uk",JP:"co.jp",US:"com"},j={CA:[],CN:[],IN:[],DE:["javari"],FR:["javari"],GB:["javari"],JP:["javari"],US:["smallparts","amazonwireless","endless","myhabit"]},F=(function(){var P=-1,O={};O.getNextSlotNum=function(){return ++P;};return O;}()),q,o,e=Math.max(document.body.scrollHeight,document.body.offsetHeight,document.documentElement.clientHeight,document.documentElement.scrollHeight,document.documentElement.offsetHeight),m=Math.max(document.body.scrollWidth,document.body.offsetWidth,document.documentElement.clientWidth,document.documentElement.scrollWidth,document.documentElement.offsetWidth),y={totalDocWidth:m,totalDocHeight:e,logType:"onetag_pageload",pageTitle:document.title},a="w50",J="w61",H="g12",C={},b=new RegExp("%3F"),w=new Object(),x=false,l="",s="",u=0,L=0,d=0,G=new RegExp("amzn.to"),r=new RegExp(h.redirectorEndPoint),E=["kdp.amazon.com"],N=[],I="assocPayloadId",c=function(P){var Q,O=false;for(Q=0;Q<E.length;Q++){if(P.match(E[Q])){O=true;break;}}return O;},p=function(O){return O.nextSibling&&O.nextSibling.tagName==="IMG"&&O.nextSibling.hasAttribute("src")&&(O.nextSibling.getAttribute("src").search(/ir-[a-z]{2}\.amazon-adsystem\.com/)>-1||O.nextSibling.getAttribute("src").search(/www\.assoc-amazon\.*/)>-1);},n=function(O){if(!O.href.match(r)){O.href=h.redirectorEndPoint+O.href;}},k=function(Y,ae){var Z=new RegExp("/(ref=[\\w]+)/?","i"),U,ad=false,P,S,T=false,X=Y.search.match(/\?tag=([^&]+)|&tag=([^&]+)|\?tag-value=([^&]+)|&tag-value=([^&]+)|\?tag_value=([^&]+)|&tag_value=([^&]+)|\?t=([^&]+)|&t=([^&]+)/),R=Y.search.match(/\?tag=|&tag=|\?tag-value=|&tag-value=|\?tag_value=|&tag_value=|\?t=|&t=/),O=Y.search.match(/(linkCode|link_code|lc)=([^&]+)/i),W=v.elementInViewPort(Y),ac={autoTagged:false,overwritten:false,geoRedirected:false,atf:W.inViewPort},Q=F.getNextSlotNum(),V={destinationURL:Y.href,slotNum:Q,atfInFirstLoad:W.inViewPort,posX:W.posX,posY:W.posY,logType:"onetag_textlink"},ab=p(Y),aa;ac.slotNum=Q;if(Y.search===""){Y.search="?imprToken="+v.getImpressionToken()+"&slotNum="+Q;}else{Y.search=Y.search.replace(/\?/,"?imprToken="+v.getImpressionToken()+"&slotNum="+Q+"&");}if(h.enableAutoTagging){ac.autoTagged=true;if(X){if(h.overwrite){for(S=1;S<9;S++){if(X[S]!=undefined){Y.search=Y.search.replace(X[S],ae);break;}}ac.overwritten=true;ad=true;}}else{if(R){Y.search=Y.search.replace(/tag=/,"tag="+ae);ad=true;}else{Y.search=Y.search.replace(/\?/,"?tag="+ae+"&");ad=true;}}}if(O&&typeof h.overridableLinkCodes[O[2]]!=="undefined"){T=true;}if(O&&!T){P=O[2];}else{P=ad?a:J;}if(O){V.oldLinkCode=O[2];Y.search=Y.search.replace(O[2],P);}else{Y.search=Y.search.replace(/\?/,"?linkCode="+P+"&");}if(ad){aa=ae;}else{if(typeof X!=="undefined"&&X instanceof Array&&X.length>=S+1&&typeof X[S]==="string"){aa=X[S];}else{aa="";}}if(C.shouldBeGeoRedirected()){ac.geoRedirected=true;n(Y);}if(Y.hasAttribute("data-amzn-asin")&&!Y.search.match("creativeASIN")){Y.search=Y.search.replace(/\?/,"?creativeASIN="+Y.getAttribute("data-amzn-asin")+"&");}if(C.shouldTrackTransit(h)){v.recordTransit();V[I]=v.getTransitId();}N.push({pos:W,slotNum:Q,linkCode:P,linkInfo:V,skipIRCall:ab,imprTag:aa});Y.href=v.addAAXClickUrl(Y.href);return ac;},A=function(O){if(O.href.match(b)){o=O.href.split(b);O.href=o[0]+"?"+decodeURIComponent(o[1]);}},t=function(P,O,S){var R,Q;for(R=0;R<P.length;R++){for(Q=0;Q<O.length;Q++){if(window.addEventListener){P[R].addEventListener(O[Q],S,false);}else{P[R].attachEvent("on"+O[Q],S);}}}},K=function(O,P){var Q=false;t([O],["touchstart"],function(){Q=false;});t([O],["touchmove"],function(){Q=true;});t([O],["click","touchend"],function(R){if(Q){return;}O.setAttribute("href",P);});t([O],["auxclick","contextmenu"],function(R){O.setAttribute("href",P);});t([O],["mouseup"],function(R){if(R.button===1||R.ctrlKey){O.setAttribute("href",P);}});},M=function(){var O="";for(i=0;i<h.itemRefs.length;i++){if(typeof h.itemRefs[i].type!=="undefined"&&h.itemRefs[i].type==="ASIN"&&typeof h.itemRefs[i].sourceLink!=="undefined"&&String(h.itemRefs[i].sourceLink).match(G)!==null&&typeof h.itemRefs[i].destinationLink!=="undefined"){w[h.itemRefs[i].sourceLink]=h.itemRefs[i].destinationLink;if(l!==""){O=",";}l=l+O+h.itemRefs[i].sourceLink;u++;}}},f=function(P,O){B.trackElements([P],function(){if(typeof O!==undefined&&O.slotNum!==undefined&&(O.viewed===undefined||!O.viewed)){v.recordViewability(O.slotNum);if(C.shouldInteractWithAES(h)){v.recordAESViewability(O.slotNum);}O.viewed=true;}});},g=function(O,P){K(O,O.getAttribute("href"));O.setAttribute("href",P);},z=function(){var Q,P,O;for(Q=0;Q<N.length;Q++){P=N[Q];O=P.pos;v.recordImpression(P.linkCode,P.imprTag,P.linkInfo,P.skipIRCall,P.slotNum);v.recordViewability(P.slotNum,O.inViewPort,O.posX,O.posY);if(C.shouldInteractWithAES(h)){v.recordAESImpression(P.linkCode,P.imprTag,P.linkInfo);v.recordAESViewability(P.slotNum,O.inViewPort,O.posX,O.posY);}}N=[];};if(h.locale!=undefined){q=h.locale;}else{q="US";}C.shouldBeGeoRedirected=function(){return h.enableGeoRedirection&&(h.region!==""&&h.region!==h.viewerCountry);};C.publisherCallBack=function(){window["amzn_assoc_client_cb_"+h.adUnitSlotNum]({type:"onload",data:{},widget:C});};C.decorateLinkElement=function(O){A(O);linkProperties=k(O,h.trackingId);f(O,linkProperties);return linkProperties;};C.shouldTrackTransit=function(O){return((typeof O.disableTransitTracking==="undefined")||!O.disableTransitTracking);};C.shouldInteractWithAES=function(O){return((typeof O.enableAESInteraction!=="undefined")&&O.enableAESInteraction);};C.tagLinks=function(af){var ah,ag,P,aa,aj,ac=[],al=0,X,Z,ai,ae,ak,O,Y,V=0,R=0,ab=0,Q=0,U=0,S=0,T,W,ad="";P=D[q];aa=j[q];aj=new RegExp("^(http|https)://(www|[\\w\\-\\.]+)?amazon\\.("+P+")/","i");if(aa){for(al=0;al<aa.length;al++){X=P;if(P=="co.jp"){X="co.jp|jp";}ac[al]=new RegExp("^(http|https)://(www\\.)?("+aa[al]+")\\.("+X+")/","i");}}Z=af.getElementsByTagName("a");if(!x){M();x=true;}for(ah=0;ah<Z.length;ah++){Y=undefined;ai=String(Z[ah].href);if(ae=ai.match(aj)&&!c(ai)){Y=C.decorateLinkElement(Z[ah]);g(Z[ah],ai);}else{if(h.isShortLinksSupported&&(ak=ai.match(G))!==null){L++;if(s!==""){ad=",";}s=s+ad+Z[ah].href;T=w[Z[ah].href];if(typeof T!=="undefined"){d++;Z[ah].setAttribute("href",T);Y=C.decorateLinkElement(Z[ah]);g(Z[ah],ai);}else{if(C.shouldBeGeoRedirected()){Y=C.decorateLinkElement(Z[ah]);g(Z[ah],ai);}}}else{for(O=0;O<ac.length;O++){if(ae=ai.match(ac[O])){C.decorateLinkElement(Z[ah]);g(Z[ah],ai);}}}}if(typeof Y!=="undefined"){if(Y.autoTagged){R++;}if(Y.overwritten){S++;}if(Y.geoRedirected){ab++;}if(Y.atf){Q++;}else{U++;}V++;}}y.numLinks=V;y.numAutoTaggedLinks=R;y.autoTaggingEnabled=h.enableAutoTagging;y.geoRedirectEnabled=h.enableGeoRedirection;y.disableTransitTracking=h.disableTransitTracking;y.numLinksATF=Q;y.numLinksBTF=U;y.shortLinksInLivePool=l;y.shortLinksInPage=s;y.shortLinksInLivePoolCount=u;y.shortLinksInPageCount=L;y.shortLinksMatchCount=d;if(C.shouldTrackTransit(h)){v.recordTransit();y[I]=v.getTransitId();}v.recordImpression(h.linkCode,h.trackingId,y);if(C.shouldInteractWithAES(h)){v.recordAESImpression(h.linkCode,h.trackingId,y);}t([window],["load"],z);};return C;};
    var spec = {
        trackingId : "teclado-20",
        region : "US",
        overwrite : false,
        enableAutoTagging : false,
        linkCode : "w49",
        overridableLinkCodes :  {   "am1": ""   , "am2": ""   , "am3": ""   , "as1": ""   , "as2": ""   , "as3": ""   , "as4": ""   , "li1": ""   , "li2": ""   , "li3": ""   , "ll1": ""   , "ll2": ""   },
        enableGeoRedirection : true,
        redirectorEndPoint : "https://assoc-redirect.amazon.com/g/r/",
        adUnitSlotNum : "0",
        itemRefs : [],
        isShortLinksSupported : true,
        viewerCountry : "IL",
        disableTransitTracking : false,
        enableAESInteraction : false
    }, trackingUtils = window.trackingUtils(
        "1",
        "//fls-na.amazon-adsystem.com/1/associates-ads/1/OP/r/json",
        "//ir-na.amazon-adsystem.com/e/ir",
        "https://aax-us-east.amazon-adsystem.com/x/px/Qi3TKwirjJKlTW2X2c-mJCoAAAFsAH77OQEAAAFKAasC1HU/", "https://aax-us-east.amazon-adsystem.com/x/c/Qi3TKwirjJKlTW2X2c-mJCoAAAFsAH77OQEAAAFKAasC1HU/", "V7r-4ClZa-71DH-SIaxFEA", undefined, undefined, undefined, true,
        "https://assoc-na.associate-amazon.com/onetag/"
    );

    window.amznAutoTagger = amznAutoTaggerMaker(spec, trackingUtils, window.elemTracker(trackingUtils));
    window.amznAutoTagger.tagLinks(document);
    window.amznAutoTagger.publisherCallBack();
}());

 //# sourceURL=dynscript-0.js</script><script type="text/javascript" src="https://api.getdrip.com/client/track?url=https%3A%2F%2Fblog.tecladocode.com%2Fpython-slices-part-2%2F&amp;visitor_uuid=c998db3b317e4fbabf67499082ff67b3&amp;_action=Visited%20twice%20in%20one%20week&amp;source=drip&amp;drip_account_id=5640782&amp;callback=Drip_138432268"></script>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <title>Python Slices Part 2: The Deep Cut</title>
    <meta name="HandheldFriendly" content="True">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link href="/assets/built/prism.css?v=79f9761232" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/tonsky/FiraCode@1.206/distr/fira_code.css">
    <link rel="stylesheet" type="text/css" href="/assets/built/screen.css?v=79f9761232">

    <meta name="description" content="In this post we take a deeper dive into Python slices, and pull back the curtain on the magic methods behind the slice notation we covered in earlier posts.">
    <link rel="shortcut icon" href="/favicon.png" type="image/png">
    <link rel="canonical" href="https://blog.tecladocode.com/python-slices-part-2/">
    <meta name="referrer" content="no-referrer-when-downgrade">
    <link rel="amphtml" href="https://blog.tecladocode.com/python-slices-part-2/amp/">
    
    <meta property="og:site_name" content="The Teclado Blog">
    <meta property="og:type" content="article">
    <meta property="og:title" content="Python Slices Part 2: The Deep Cut">
    <meta property="og:description" content="In this post we take a deeper dive into Python slices, and pull back the curtain on the magic methods behind the slice notation we covered in earlier posts.">
    <meta property="og:url" content="https://blog.tecladocode.com/python-slices-part-2/">
    <meta property="og:image" content="https://blog.tecladocode.com/content/images/2019/04/citric-citrus-color-997725.jpg">
    <meta property="article:published_time" content="2019-04-14T08:30:00.000Z">
    <meta property="article:modified_time" content="2019-05-02T23:46:07.000Z">
    <meta property="article:tag" content="Learn Python Programming">
    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Python Slices Part 2: The Deep Cut">
    <meta name="twitter:description" content="In this post we take a deeper dive into Python slices, and pull back the curtain on the magic methods behind the slice notation we covered in earlier posts.">
    <meta name="twitter:url" content="https://blog.tecladocode.com/python-slices-part-2/">
    <meta name="twitter:image" content="https://blog.tecladocode.com/content/images/2019/04/citric-citrus-color-997725.jpg">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Phil Best">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="Learn Python Programming">
    <meta name="twitter:site" content="@tecladocode">
    <meta name="twitter:creator" content="@PhilBest2202">
    <meta property="og:image:width" content="1920">
    <meta property="og:image:height" content="1080">
    
    <script type="text/javascript" async="" src="//tag.getdrip.com/5640782.js"></script><script async="" src="https://connect.facebook.net/en_US/fbevents.js"></script><script async="" src="https://www.google-analytics.com/analytics.js"></script><script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Article",
    "publisher": {
        "@type": "Organization",
        "name": "The Teclado Blog",
        "logo": "https://blog.tecladocode.com/content/images/2019/05/logo-white.svg"
    },
    "author": {
        "@type": "Person",
        "name": "Phil Best",
        "image": {
            "@type": "ImageObject",
            "url": "https://blog.tecladocode.com/content/images/2019/03/IMG_20160610_153242--2-.jpg",
            "width": 1900,
            "height": 1900
        },
        "url": "https://blog.tecladocode.com/author/phil/",
        "sameAs": [
            "https://twitter.com/PhilBest2202"
        ]
    },
    "headline": "Python Slices Part 2: The Deep Cut",
    "url": "https://blog.tecladocode.com/python-slices-part-2/",
    "datePublished": "2019-04-14T08:30:00.000Z",
    "dateModified": "2019-05-02T23:46:07.000Z",
    "image": {
        "@type": "ImageObject",
        "url": "https://blog.tecladocode.com/content/images/2019/04/citric-citrus-color-997725.jpg",
        "width": 1920,
        "height": 1080
    },
    "keywords": "Learn Python Programming",
    "description": "In this post we take a deeper dive into Python slices, and pull back the curtain on the magic methods behind the slice notation we covered in earlier posts.",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://blog.tecladocode.com/"
    }
}
    </script>

    <script src="/public/ghost-sdk.min.js?v=79f9761232"></script>
<script>
ghost.init({
	clientId: "ghost-frontend",
	clientSecret: "de7265ddb61e"
});
</script>
    <meta name="generator" content="Ghost 2.21">
    <link rel="alternate" type="application/rss+xml" title="The Teclado Blog" href="https://blog.tecladocode.com/rss/">
    <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-44054919-14', 'auto');
  ga('send', 'pageview');

</script>

<style>
    .site-title .site-logo {
        margin-bottom: 10px;
    }
    
    pre {
        margin-bottom: 21px;
    }
    
    .banner {
        border: 2px solid black;
        padding: 3em 3em 1.5em 3em;
        margin: .5em 0;
        font-size: 80%;
        border-radius: 5px;
    }
    
    .banner.info {
        border: 2px solid #26E38A;
        background-color: #26E38A10;
    }
    
    form.drip-form {
        font-size: 1.5rem;
        background-color: #f1f1f1;
        padding: 16px;
        border-radius: 3px;
        font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;
    }
    
    form.drip-form h3 {
    }
    
    form.drip-form label {
        font-size: 2rem;
        font-weight: 500;
        
        margin-right: 6px;
    }
    
    form.drip-form input[type="submit"] {
        background-color: #26E38A;
        border: none;
        border-radius: 6px;
        padding: 8px 16px;
        margin-top: 12px;
        font-weight: 500;
        font-size: 2rem;
    }
    
    form.drip-form input[type="email"]:focus {
        border: 2px solid #26E38A;
    }
    
    form.drip-form input[type="submit"]:hover {
        border-color: #26E38A;
    }
    
    form.drip-form input[type="email"] {
        background-color: #d5d5d5;
        border: 2px solid;
        border-radius: 3px;
        padding: 6px 10px;
        font-size: 1.5rem;
        width: 25rem;
    }
    
</style>
<!-- Facebook Pixel Code -->
<script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', '231005443993372');
  fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
  src="https://www.facebook.com/tr?id=231005443993372&ev=PageView&noscript=1"
/></noscript>
<!-- End Facebook Pixel Code -->

<style id="fit-vids-style">.fluid-width-video-container{flex-grow: 1;width:100%;}.fluid-width-video-wrapper{width:100%;position:relative;padding:0;}.fluid-width-video-wrapper iframe,.fluid-width-video-wrapper object,.fluid-width-video-wrapper embed {position:absolute;top:0;left:0;width:100%;height:100%;}</style><style type="text/css">
  /* === Form-Specific Styles === */
  /* stylelint-disable */

  #drip-121349 {
  }

  #drip-121349 .drip-header {
    background-color: #000000 !important;
  }

  #drip-121349 .drip-content h3 {
    color: #000000 !important;
    font-size: 23px !important;
  }

  #drip-121349 .drip-submit-button {
    background-color: #000000 !important;
    font-size: 15px !important;
  }

  #drip-121349 .drip-submit-button:hover {
    background-color: #000000 !important;
  }

  #drip-121349 .drip-submit-button:active {
    background-color: #000000 !important;
  }

  #drip-121349 dl dt,
  #drip-121349 .drip-content .drip-description,
  #drip-121349 .drip-errors {
    font-size: 14px !important;
  }

  #drip-121349 .drip-text-field {
    font-size: 14px !important;
  }

  /* === Reset styles === */

  .drip-tab h1,
  .drip-tab h2,
  .drip-tab h3,
  .drip-tab div,
  .drip-tab dl,
  .drip-tab dt,
  .drip-tab dd,
  .drip-tab p,
  .drip-tab a,
  .drip-tab .drip-text-field,
  .drip-tab .drip-text-field:focus,
  .drip-tab .drip-submit-button {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
    float: none;
    width: auto;
    background-image: none;
    letter-spacing: 0;
    -webkit-box-shadow: none;
       -moz-box-shadow: none;
            box-shadow: none;
    -webkit-text-shadow: none !important;
       -moz-text-shadow: none !important;
            text-shadow: none !important;
  }

  .drip-tab a {
    text-decoration: none;
    color: #000000 !important;
  }

  .drip-tab :focus {
    outline: 0;
  }

  /* === Clearfix === */

  .drip-clearfix:after {
    visibility: hidden;
    display: block;
    font-size: 0;
    content: " ";
    clear: both;
    height: 0;
  }
  * html .drip-clearfix             { zoom: 1; } /* IE6 */
  *:first-child+html .drip-clearfix { zoom: 1; } /* IE7 */

  /* === Main Container === */

  .drip-tab-container * {
    box-sizing: content-box;
  }

  /* === Content === */

  .drip-tab .drip-content {
    margin: 0;
    padding: 0;
    width: 380px;
    position: fixed;
    font-size: 100%;
    font: inherit;
    z-index: 10000;
    color: #333;
    vertical-align: baseline;
    text-align: left;
    background-color: #ffffff;
    -webkit-box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
       -moz-box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
            box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
  }

  .drip-tab.bottom .drip-content {
    bottom: -800px;
    -webkit-border-radius: 8px 8px 0 0;
       -moz-border-radius: 8px 8px 0 0;
            border-radius: 8px 8px 0 0;
    -webkit-transition: bottom 200ms ease-in;
       -moz-transition: bottom 200ms ease-in;
         -o-transition: bottom 200ms ease-in;
            transition: bottom 200ms ease-in;
  }

  .drip-tab.bottom.left .drip-content {
    left: 40px;
  }

  .drip-tab.bottom.right .drip-content {
    right: 40px;
  }

  .drip-tab.side-image .drip-content {
    width: 650px;
  }

  .drip-tab.side .drip-content {
    top: 10%;
  }

  .drip-tab.side.right .drip-content {
    right: -675px;
    -webkit-border-radius: 8px 0 0 8px;
       -moz-border-radius: 8px 0 0 8px;
            border-radius: 8px 0 0 8px;
    -webkit-transition: right 200ms ease-in;
       -moz-transition: right 200ms ease-in;
         -o-transition: right 200ms ease-in;
            transition: right 200ms ease-in;
  }

  .drip-tab.side.left .drip-content {
    left: -675px;
    -webkit-border-radius: 0 8px 8px 0;
       -moz-border-radius: 0 8px 8px 0;
            border-radius: 0 8px 8px 0;
    -webkit-transition: left 200ms ease-in;
       -moz-transition: left 200ms ease-in;
         -o-transition: left 200ms ease-in;
            transition: left 200ms ease-in;
  }

  .drip-tab.mobile .drip-content {
    width: 100% !important;
    bottom: -800px;
    left: 0;
    -webkit-border-radius: 0;
       -moz-border-radius: 0;
            border-radius: 0;
    -webkit-transition: bottom 200ms ease-in;
       -moz-transition: bottom 200ms ease-in;
         -o-transition: bottom 200ms ease-in;
            transition: bottom 200ms ease-in;
  }

  .drip-tab.drip-scrollable .drip-content {
    overflow-y: scroll;
  }

  /* === Header === */

  .drip-tab .drip-header {
    margin: 0;
    padding: 0;
    position: fixed;
    font-size: 100%;
    font: inherit;
    z-index: 10000;
    color: #333;
    vertical-align: baseline;
    text-align: left;
    -webkit-border-radius: 8px 8px 0 0;
       -moz-border-radius: 8px 8px 0 0;
            border-radius: 8px 8px 0 0;
    -webkit-box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
       -moz-box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
            box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
  }

  .drip-tab.bottom .drip-header {
    width: 380px;
    bottom: 0;
    -webkit-transition: bottom 200ms ease-in;
       -moz-transition: bottom 200ms ease-in;
         -o-transition: bottom 200ms ease-in;
            transition: bottom 200ms ease-in;
  }

  .drip-tab.bottom .drip-header.drip-hidden {
    bottom: -800px;
  }

  .drip-tab.bottom.left .drip-header {
    left: 40px;
  }

  .drip-tab.bottom.right .drip-header {
    right: 40px;
  }

  .drip-tab.bottom.image-left .drip-header,
  .drip-tab.bottom.image-right .drip-header {
    width: 510px;
  }

  .drip-tab.side .drip-header {
    width: 340px;
    top: 10%;
  }

  .drip-tab.side.right .drip-header {
    right: -100px;
    -webkit-transition: right 400ms ease-in;
       -moz-transition: right 400ms ease-in;
         -o-transition: right 400ms ease-in;
            transition: right 400ms ease-in;
    -webkit-transform: rotate(-90deg) !important;
       -moz-transform: rotate(-90deg) !important;
        -ms-transform: rotate(-90deg) !important;
         -o-transform: rotate(-90deg) !important;
            transform: rotate(-90deg) !important;
    -webkit-transform-origin: right center;
       -moz-transform-origin: right center;
         -o-transform-origin: right center;
            transform-origin: right center;
  }

  .drip-tab.side.right .drip-header.drip-hidden {
    right: -100px;
  }

  .drip-tab.side.left .drip-header {
    left: -100px;
    -webkit-transition: left 400ms ease-in;
       -moz-transition: left 400ms ease-in;
         -o-transition: left 400ms ease-in;
            transition: left 400ms ease-in;
    -webkit-transform: rotate(90deg) !important;
       -moz-transform: rotate(90deg) !important;
        -ms-transform: rotate(90deg) !important;
         -o-transform: rotate(90deg) !important;
            transform: rotate(90deg) !important;
    -webkit-transform-origin: left center;
       -moz-transform-origin: left center;
         -o-transform-origin: left center;
            transform-origin: left center;
  }

  .drip-tab.side.left .drip-header.drip-hidden {
    left: -100px;
  }

  .drip-tab.mobile .drip-header {
    width: 100% !important;
    bottom: 0;
    left: 0;
    -webkit-border-radius: 0;
       -moz-border-radius: 0;
            border-radius: 0;
    -webkit-transition: bottom 200ms ease-in;
       -moz-transition: bottom 200ms ease-in;
         -o-transition: bottom 200ms ease-in;
            transition: bottom 200ms ease-in;
  }

  .drip-tab.mobile .drip-header.drip-hidden {
    bottom: -300px;
  }

  /* === Header Toggle === */

  .drip-tab .drip-toggle {
    display: block;
    text-decoration: none;
    padding: 10px 50px 10px 25px; /* extra padding for the arrow */
  }

  /* === Teaser === */

  .drip-tab .drip-header h2 {
    display: block;
    margin: 0 !important;
    padding: 0 !important;
    border: 0 !important;
    font-size: 16px !important;
    line-height: 1.5 !important;
    font-weight: bold !important;
    text-align: left !important;
    color: #fff !important;
    clear: none !important;
    letter-spacing: 0 !important;
    width: auto !important;
  }

  /* === Arrows === */

  .drip-tab .drip-header span.drip-arrow {
    display: block;
    position: absolute;
    margin: 0;
    padding: 0;
    width: 0;
    height: 0;
    line-height: 0;
    top: 20px;
    right: 32px;
  }

  /* === Panel === */

  .drip-tab .drip-content > div.drip-panel {
    padding: 25px;
    background-color: #fff;
    -webkit-border-radius: 6px;
       -moz-border-radius: 6px;
            border-radius: 6px;
  }

  .drip-tab.bottom .drip-content > div.drip-panel {
    -webkit-border-radius: 6px 6px 0 0;
       -moz-border-radius: 6px 6px 0 0;
            border-radius: 6px 6px 0 0;
  }

  .drip-tab.side.left .drip-content > div.drip-panel {
    -webkit-border-radius: 0 6px 6px 0;
       -moz-border-radius: 0 6px 6px 0;
            border-radius: 0 6px 6px 0;
  }

  .drip-tab.side.right .drip-content > div.drip-panel  {
    -webkit-border-radius: 6px 0 0 6px;
       -moz-border-radius: 6px 0 0 6px;
            border-radius: 6px 0 0 6px;
  }

  /* === Powered By === */

  .drip-tab .drip-powered-by {
    padding: 8px;
    text-align: left;
    font-weight: normal;
    font-size: 10px;
    line-height: 16px;
    color: #A8ACB9;
    text-align: right;
    margin-right: 25px;
    text-transform: uppercase;
    display: -webkit-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;
    justify-content: flex-end;
    align-items: center;
  }

  .drip-tab .drip-powered-by a {
    color: #A8ACB9 !important;
    text-decoration: underline !important;
    margin-left: 6px;
  }

  /* === Content Sections === */

  .drip-tab.side-image .drip-form-aside {
    width: 245px;
    text-align: center;
  }

  .drip-tab.image-left .drip-form-main {
    margin-left: 270px;
  }

  .drip-tab.image-right .drip-form-main {
    margin-right: 270px;
  }

  .drip-tab.image-left .drip-form-aside {
    float: left;
  }

  .drip-tab.image-right .drip-form-aside {
    float: right;
  }

  @media screen and (max-width: 650px) {
    .drip-tab.side-image .drip-content {
      width: 380px;
    }

    .drip-tab.side-image .drip-form-main {
      margin-left: 0;
      margin-right: 0;
    }

    .drip-tab.side-image .drip-form-aside {
      display: none;
    }
  }

  /* === Content Headings & Paragraphs === */

  .drip-tab .drip-content h3 {
    display: block;
    margin: 0 20px 0 0 !important;
    padding: 0 0 15px 0 !important;
    line-height: 1.4 !important;
    font-weight: bold !important;
    text-align: left !important;
    color: #4477bd !important;
    clear: none !important;
  }

  .drip-tab .drip-content .drip-description {
    margin: 0;
    padding: 0 0 20px 0;
    line-height: 1.4;
    text-align: left;
    color: #4F5362;
  }

  .drip-tab .drip-content .drip-post-submission {
    padding: 0;
  }

  .drip-tab .drip-content .drip-description a {
    text-decoration: underline;
  }

  .drip-tab .drip-content .drip-description em {
    font-style: italic;
  }

  .drip-tab .drip-content .drip-description ul,
  .drip-tab .drip-content .drip-description ol {
    list-style-position: outside;
    margin: 8px 0 8px 30px;
  }

  .drip-tab .drip-content .drip-description ul li
  .drip-tab .drip-content .drip-description ol li {
    padding: 0;
  }

  .drip-tab .drip-content .drip-image-center-helper {
    display: inline-block;
    height: 100%;
    vertical-align: middle;
  }

  .drip-tab .drip-content img.drip-image {
    max-width: 245px;
    vertical-align: middle;
  }

  .drip-tab .drip-content a.drip-close {
    position: absolute;
    right: 25px;
    top: 25px;
  }

  .drip-tab .drip-content a.drip-close:hover {
    cursor: pointer;
  }

  /* === Content Subscribe Form === */

  .drip-tab form {
    margin: 0 !important;
    padding: 0 !important;
  }

  .drip-tab dl {
    display: block;
    margin: 0;
    padding: 0 0 5px 0;
  }

  .drip-tab dl dt {
    display: block;
    padding: 0 0 5px 0;
    font-weight: bold;
    color: #4F5362;
  }

  .drip-tab dl.no-labels dt {
    display: none;
  }

  .drip-tab dl dd {
    display: block;
    padding: 0 0 8px 0;
  }

  .drip-tab .drip-text-field {
    margin: 0 !important;
    padding: 10px 12px !important;
    height: auto !important;
    width: 100% !important;
    color: #4F5362 !important;
    background-color: #fff !important;
    border: 1px solid #A8ACB9 !important;
    -webkit-border-radius: 3px !important;
       -moz-border-radius: 3px !important;
            border-radius: 3px !important;
    -webkit-box-sizing: border-box !important;
       -moz-box-sizing: border-box !important;
        -ms-box-sizing: border-box !important;
            box-sizing: border-box !important;
    background-image: none !important;
    min-width: 0 !important;
    min-height: 0 !important;
  }

  .drip-tab .drip-text-field::-webkit-input-placeholder { /* WebKit browsers */
    color: #A8ACB9 !important;
  }
  .drip-tab .drip-text-field:-moz-placeholder { /* Mozilla Firefox 4 to 18 */
    color: #A8ACB9 !important;
  }
  .drip-tab .drip-text-field::-moz-placeholder { /* Mozilla Firefox 19+ */
    color: #A8ACB9 !important;
  }
  .drip-tab .drip-text-field:-ms-input-placeholder { /* Internet Explorer 10+ */
    color: #A8ACB9 !important;
  }

  .drip-tab .drip-text-field:focus {
    border-color: #9398a9 !important;
    outline: 0;
    background-image: none;
    background-color: #fff !important;
  }

  .drip-tab.mobile .drip-text-field {
    font-size: 16px;
  }

  .drip-tab .drip-errors {
    padding: 5px 0 0 0;
    font-weight: normal;
    color: red;
  }

  .drip-tab .drip-submit-button {
    padding: 6px 26px !important;
    color: #ffffff !important;
    font-weight: bold !important;
    line-height: 1.6 !important;
    border: 0 !important;
    -webkit-border-radius: 3px !important;
       -moz-border-radius: 3px !important;
            border-radius: 3px !important;
    cursor: pointer !important;
    background-image: none !important;
    min-width: 0 !important;
    min-height: 0 !important;
    height: auto;
    transition: background 0.2s ease !important;
  }

  .drip-tab .drip-submit-button:hover {
    background-image: none !important;
  }

  .drip-tab .drip-submit-button:active {
    background-image: none !important;
  }

  /* checkbox */

  .drip-tab input,
  .drip-tab textarea {
    display: block;
    box-shadow: none;
    position: relative;
    border: 1px solid #cccccc;
    outline: none;
    border-radius: 3px;
    font: inherit;
    color: #262626;
    padding: 12px 18px;
    transition: border-color 300ms;
    width: 100%;
  }

  .drip-tab .zenput--checkbox.hidden {
    margin-bottom: -8px;
    display: none;
  }

  .drip-tab .zenput--checkbox input[type="checkbox"] {
    height: 0;
    width: 0;
    opacity: 0;
    position: absolute;
    top: 0;
    left: 0;
  }

  .drip-tab .zenput--checkbox input[type="checkbox"] ~ .zenput__checkbox-label {
    font: inherit;
    font-size: 16px;
    line-height: 30px;
    color: #262626;
    cursor: pointer;
    white-space: normal;
    word-break: normal;
    display: block;
    padding-left: 36px;
    position: relative;
    transition: color 300ms
  }

  .drip-tab .zenput--checkbox input[type="checkbox"]~ .zenput__checkbox-label .zenput__checkbox-label__icon {
    content: "";
    display: block;
    background: #f5f5f5;
    width: 24px;
    height: 24px;
    position: absolute;
    top: 3px;
    left: 0;
    border-radius: 3px;
    border: 1px solid #cccccc;
    box-sizing: border-box;
    padding: 3px;
    transition: background 300ms ease-out, border-color 300ms;
  }

  .drip-tab .zenput--checkbox input[type="checkbox"] ~ .zenput__checkbox-label .zenput__checkbox-label__icon svg {
    opacity: 0;
    width: 16px;
    display: block;
    fill: #cccccc;
    transition: opacity 300ms ease-out;
  }

  .drip-tab .zenput--checkbox input[type="checkbox"]:checked ~ .zenput__checkbox-label {
    color: #333 !important;
  }
  .drip-tab .zenput--checkbox input[type="checkbox"]:checked ~ .zenput__checkbox-label .zenput__checkbox-label__icon {
    background-color: #ffffff;
    border-color: #a8acb9;
  }
  .drip-tab .zenput--checkbox input[type="checkbox"]:checked ~ .zenput__checkbox-label .zenput__checkbox-label__icon svg {
    fill: #000000 !important;
    opacity: 1;
  }

  /* hover state */

  .drip-tab .zenput--checkbox input:not([disabled]):not(:checked) ~ .zenput__checkbox-label:hover {
    color: #262626;
  }

  .drip-tab .zenput--checkbox input:not([disabled]):not(:checked) ~ .zenput__checkbox-label:hover  .zenput__checkbox-label__icon {
    border-color: var(--gray-9);
  }

  .drip-tab .zenput--checkbox input:not([disabled]):not(:checked) ~ .zenput__checkbox-label:hover  .zenput__checkbox-label__icon svg {
    opacity: 1;
  }

  /* active state */

  .drip-tab .zenput--checkbox input:not([disabled]) ~ .zenput__checkbox-label:active {
    color: #f224f2;
  }

  /* focus state */

  .drip-tab .zenput--checkbox input:not([disabled]) ~ .zenput__checkbox-label:focus .zenput__checkbox-label__icon,
  .drip-tab .zenput--checkbox input:not([disabled]):focus ~ .zenput__checkbox-label .zenput__checkbox-label__icon {
    border-color: #262626;
  }

  /* stylelint-enable */

</style><style>.amlk_notification,
.amlk_notification_container {
    margin-right: 3px !important;
    margin-left: 0px !important;
}

.amlk_popup {
    direction: rtl;
}

.amlk_popup-arrow {
    right: auto;
    left: -14px;
}

.amlk_popup-text li {
    text-align: right;
}

.amlk_popup-text li .amlk_popup-text-name {
    float: right;
}

.amlk_popup-text li .amlk_popup-text-user-score {
    float: right;
    margin-right: 0px;
    margin-left: 5px;
}

.amlk_up-vote, .amlk_down-vote {
    left: 7px;
    right: auto;
}

.amlk_popup-text li .amlk_popup-text-score {
    left: 0px;
    right: auto;
}

.amlk_popup-text li:first-child .amlk_popup-text-user-score {
    margin-right: 3px;
    margin-left: 0px;
}

.amlk_popup-text li:first-child .amlk_up-vote, .amlk_popup-text li:first-child .amlk_down-vote{
    left: 5px;
    right: auto;
}</style></head>

<body class="post-template tag-learn-python-programming">

    <div class="site-wrapper">

        



<style type="text/css">
.responsive-header-img {
    background-image: url(/content/images/size/w2000/2019/04/citric-citrus-color-997725.jpg);
}
.header-image-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.65);
}
@media(max-width: 1000px) {
    .responsive-header-img {
        background-image: url(/content/images/size/w1000/2019/04/citric-citrus-color-997725.jpg);
        background-image: -webkit-image-set(
                url(/content/images/size/w1000/2019/04/citric-citrus-color-997725.jpg) 1x,
                url(/content/images/size/w2000/2019/04/citric-citrus-color-997725.jpg) 2x
        );
        background-image: image-set(
                url(/content/images/size/w1000/2019/04/citric-citrus-color-997725.jpg) 1x,
                url(/content/images/size/w2000/2019/04/citric-citrus-color-997725.jpg) 2x
        );
    }
}
@media(max-width: 600px) {
    .responsive-header-img {
        background-image: url(/content/images/size/w600/2019/04/citric-citrus-color-997725.jpg);
        background-image: -webkit-image-set(
                url(/content/images/size/w600/2019/04/citric-citrus-color-997725.jpg) 1x,
                url(/content/images/size/w1000/2019/04/citric-citrus-color-997725.jpg) 2x
        );
        background-image: image-set(
                url(/content/images/size/w600/2019/04/citric-citrus-color-997725.jpg) 1x,
                url(/content/images/size/w1000/2019/04/citric-citrus-color-997725.jpg) 2x
        );
    }
}
</style>
<header class="site-header outer responsive-header-img">
    <div class="header-image-overlay"></div>

 
<nav class="site-nav">
    <div class="site-nav-left">
            <a class="site-nav-logo" href="https://blog.tecladocode.com"><img src="/content/images/2019/05/logo-white.svg" alt="The Teclado Blog"></a>
    </div>
    <div class="site-nav-right">
            <ul class="nav" role="menu">
    <li class="nav-start-learning-python" role="menuitem"><a href="https://blog.tecladocode.com/how-to-start-learning-python/">Start Learning Python</a></li>
    <li class="nav-the-linux-console" role="menuitem"><a href="https://blog.tecladocode.com/understanding-the-linux-console/">The Linux Console</a></li>
</ul>

    </div>
</nav>
<div class="inner">
    <div class="site-header-content">
        <span class="post-primary-tag">Learn Python Programming</span>
        <h1 class="site-title">Python Slices Part 2: The Deep Cut</h1>
        <div class="post-info">
            <div class="author-avatar-name">
                <a href="/author/phil/" class="static-avatar">
                    <img class="author-profile-image" src="/content/images/size/w100/2019/03/IMG_20160610_153242--2-.jpg">
                </a>
                <div class="post-info">
                    <span class="author-name"><a href="/author/phil/">Phil Best</a></span>
                    <div class="post-metadata">
                        <span class="reading-time">4 min read</span> ·
                        <time class="post-full-meta-date" datetime="2019-04-14">Apr 14</time>
                    </div>
                </div>
            </div>
        </div>

    </div>
</div>
</header>


<main id="site-main" class="site-main outer">
    <div class="inner">

        <article class="post-full post tag-learn-python-programming ">

            <section class="post-full-content">
                <div class="post-content">
                    <p>In this post, we're going to do a slightly deeper dive into slices in Python. If you need a refresher on the basics, be sure to check out our <a href="http://blog.tecladocode.com/python-slices/">earlier post on the topic</a>!</p><p>Without further ado, let's dive right in.</p><h2 id="slice-assignment">Slice Assignment</h2><p>In the last post, we talked a lot about grabbing some slice of a sequence, but we can actually do a great deal more with slices.</p><p>One interesting thing we can do is replace some slice of a sequence with new values.</p><!--kg-card-begin: markdown--><pre class=" language-python"><code class=" language-python">numbers <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">]</span>
numbers<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">:</span><span class="token number">2</span><span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">2</span><span class="token punctuation">]</span>

<span class="token keyword">print</span><span class="token punctuation">(</span>numbers<span class="token punctuation">)</span>  <span class="token comment"># [1, 2, 3]</span>
</code></pre>
<!--kg-card-end: markdown--><p>Here we take a slice of <code>numbers</code> which includes only the value at index 1. Remember that the stop index for slices is <strong>not inclusive</strong>.</p><p>We then use this slice as the left-hand side of an assignment. When we print <code>numbers</code>, we can see that it now reads <code>[1, 2, 3]</code> showing that the <code>3</code> at index 1 has been replaced.</p><p>One interesting thing to note is that we assigned another iterable, not just the integer <code>2</code>. We could have actually used a tuple or even a set here instead of a list:</p><!--kg-card-begin: markdown--><pre class=" language-python"><code class=" language-python">numbers<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">:</span><span class="token number">2</span><span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">,</span><span class="token punctuation">)</span>  <span class="token comment"># Don't forget the comma!</span>
numbers<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">:</span><span class="token number">2</span><span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token punctuation">{</span><span class="token number">2</span><span class="token punctuation">}</span>
</code></pre>
<!--kg-card-end: markdown--><p>However, assigning an integer would have raised a <code>TypeError</code>.</p><!--kg-card-begin: code--><pre><code>TypeError: can only assign an iterable
</code></pre><!--kg-card-end: code--><h3 id="assigning-multiple-values">Assigning Multiple Values</h3><p>As we have to assign some iterable type, it stands to reason we can assign multiple values in one go. That's absolutely correct:</p><!--kg-card-begin: markdown--><pre class=" language-python"><code class=" language-python">numbers <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">]</span>
numbers<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">:</span><span class="token number">3</span><span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">]</span>

<span class="token keyword">print</span><span class="token punctuation">(</span>numbers<span class="token punctuation">)</span>  <span class="token comment"># [1, 2, 3]</span>
</code></pre>
<!--kg-card-end: markdown--><p>However, what might surprise you is that we can assign an iterable of a different length to our slice.</p><!--kg-card-begin: markdown--><pre class=" language-python"><code class=" language-python">numbers <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">]</span>
numbers<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">:</span><span class="token number">3</span><span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">4</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">]</span>

<span class="token keyword">print</span><span class="token punctuation">(</span>numbers<span class="token punctuation">)</span> <span class="token comment"># [1, 2, 3, 4, 5]</span>
</code></pre>
<!--kg-card-end: markdown--><p>It actually makes no difference how many items our iterable contains: we can even assign an empty list to some slice without issues. The items at the indexes defined in our slice are simply removed.</p><!--kg-card-begin: markdown--><pre class=" language-python"><code class=" language-python">numbers<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">:</span><span class="token number">3</span><span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token punctuation">]</span>
</code></pre>
<!--kg-card-end: markdown--><h3 id="zero-length-slices">Zero Length Slices</h3><p>We can also exploit the uneven assignment in other ways. For example, we can take an empty slice and use it to insert values in the middle of some sequence.</p><!--kg-card-begin: markdown--><pre class=" language-python"><code class=" language-python">numbers <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">]</span>
numbers<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">:</span><span class="token number">1</span><span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">4</span><span class="token punctuation">]</span>

<span class="token keyword">print</span><span class="token punctuation">(</span>numbers<span class="token punctuation">)</span>  <span class="token comment"># [1, 2, 3, 4, 5]</span>
</code></pre>
<!--kg-card-end: markdown--><p>Remember that a slice like <code>[1:1]</code> is totally valid, but completely empty. It starts at index 1, and ends at index 1, but the stop value is not inclusive, so the value at index 1 is not part of the slice.</p><p>A slice like this therefore allows us to insert values at a given index without removing any values in the sequence.</p><h3 id="extended-slicing-and-assignment">Extended Slicing and Assignment</h3><p>In the last article, we spoke about extended slicing, using a step value. We can still perform assignment on slices on this type, but there is a caveat. Unfortunately, if we specify any step value other than the default <code>1</code>, we can't use the asymmetrical assignment we've been talking about above. This includes a step of <code>-1</code>.</p><p>As such, when we're using extended slice syntax, we need to be careful to match the number of values we want to replace.</p><!--kg-card-begin: markdown--><pre class=" language-python"><code class=" language-python">numbers <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">]</span>
numbers<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">:</span><span class="token number">4</span><span class="token punctuation">:</span><span class="token number">2</span><span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">4</span><span class="token punctuation">]</span>

<span class="token keyword">print</span><span class="token punctuation">(</span>numbers<span class="token punctuation">)</span>  <span class="token comment"># [1, 2, 3, 4, 5]</span>
</code></pre>
<!--kg-card-end: markdown--><p>The example above works just fine, because we assign <code>2</code> to index 1, and <code>4</code> to index 3. Everything matches.</p><!--kg-card-begin: markdown--><pre class=" language-python"><code class=" language-python">numbers <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">]</span>
numbers<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">:</span><span class="token number">3</span><span class="token punctuation">:</span><span class="token number">2</span><span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">4</span><span class="token punctuation">]</span>

<span class="token keyword">print</span><span class="token punctuation">(</span>numbers<span class="token punctuation">)</span>  <span class="token comment"># ValueError</span>
</code></pre>
<!--kg-card-end: markdown--><p>On the other hand, this second example produces a <code>ValueError</code>:</p><!--kg-card-begin: code--><pre><code>ValueError: attempt to assign sequence of size 2 to extended slice
</code></pre><!--kg-card-end: code--><h2 id="slice-objects-and-__getitem__">Slice Objects and <strong><code>__getitem__</code></strong></h2><p>When we first started talking about slices, we began by introducing slice objects, and the <code>slice(1, 2)</code> syntax. We used this for a little while before moving on to the shorthand we've been using in the examples above.</p><p>We've actually seen a number of ways to take a slice of some sequence:</p><!--kg-card-begin: markdown--><pre class=" language-python"><code class=" language-python">numbers <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">]</span>
new_slice <span class="token operator">=</span> <span class="token builtin">slice</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">)</span>

a <span class="token operator">=</span> numbers<span class="token punctuation">[</span>new_slice<span class="token punctuation">]</span>
b <span class="token operator">=</span> numbers<span class="token punctuation">[</span><span class="token builtin">slice</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">)</span><span class="token punctuation">]</span>
c <span class="token operator">=</span> numbers<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">:</span><span class="token number">3</span><span class="token punctuation">]</span>
</code></pre>
<!--kg-card-end: markdown--><p>These are all absolutely identical in terms of functionality. If we printed any of <code>a</code>, <code>b</code>, or <code>c</code>, we'd get <code>[2, 3]</code> printed to the console.</p><p>However, this square brackets syntax is only a convenience. What's actually happening is this:</p><!--kg-card-begin: markdown--><pre class=" language-python"><code class=" language-python">d <span class="token operator">=</span> numbers<span class="token punctuation">.</span>__getitem__<span class="token punctuation">(</span><span class="token builtin">slice</span><span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">)</span><span class="token punctuation">)</span>

<span class="token keyword">print</span><span class="token punctuation">(</span>d<span class="token punctuation">)</span>  <span class="token comment"># [2, 3]</span>
</code></pre>
<!--kg-card-end: markdown--><p>The slightly arcane looking <code>__getitem__</code> is one of Python's many special methods, often called "dunder" (double underscore) methods.</p><p>What's interesting about this, is that we can use these special methods in our own classes, which means we can also provide slicing support for our own custom types.</p><p><code>__getitem__</code> actually accepts more than just slices. We could also pass in a single index to <code>__getitem__</code>, which is exactly what happens when we do something like this: <code>numbers[0]</code>.</p><!--kg-card-begin: markdown--><pre class=" language-python"><code class=" language-python">numbers <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token number">4</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">]</span>

<span class="token keyword">print</span><span class="token punctuation">(</span>numbers<span class="token punctuation">[</span><span class="token number">2</span><span class="token punctuation">]</span><span class="token punctuation">)</span>  <span class="token comment"># 3</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>numbers<span class="token punctuation">.</span>__getitem__<span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token punctuation">)</span>  <span class="token comment"># 3</span>
</code></pre>
<!--kg-card-end: markdown--><p><code>__getitem__</code> also has a counterpart called <code>__setitem__</code>, which is called when we do slice assignment, or when we try to replace a value at a given index using subscript notation with single indexes:</p><!--kg-card-begin: markdown--><pre class=" language-python"><code class=" language-python">numbers <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span> <span class="token number">2</span><span class="token punctuation">,</span> <span class="token number">3</span><span class="token punctuation">,</span> <span class="token string">"hello"</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">]</span>
numbers<span class="token punctuation">[</span><span class="token number">3</span><span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token number">4</span>  <span class="token comment"># numbers.__setitem__(3, 4)</span>

<span class="token keyword">print</span><span class="token punctuation">(</span>numbers<span class="token punctuation">)</span>  <span class="token comment"># [1, 2, 3, 4, 5]</span>
</code></pre>
<!--kg-card-end: markdown--><p>Special methods are a large and relatively advanced topic, so don't worry if you're a little confused at this point. Special methods will be getting suitably special treatment in a future blog post, so stick around if you're interested in learning more about them!</p><h2 id="recap">Recap</h2><ul><li>In addition to using slices to grab a range of values from a sequence, we can also use slices to replace values in a sequence as part of an assignment operation.</li><li>We have to use an iterable type when assigning using a slice. This can be anything from list and tuples to sets.</li><li>Slice assignment can be asymmetrical: the length of the slice can be different to that of the iterable object we want to assign.</li><li>We can define a slice of zero length by specifying a start and stop value at the same index. We can use an empty slice to insert an arbitrary number of values at a given index.</li><li>When using extended slicing, any step value except <code>1</code> imposes some caveats on slice assignment. When using a different step size, the number of items we assign must match the number of items in the slice.</li><li>The subscript notation we use for slicing is actually shorthand for the <code>__getitem__</code> and <code>__setitem__</code> special methods. This is very useful, because it means we can define slicing behaviour for our own custom types.</li></ul>
                </div>
            </section>


            <footer class="post-full-footer">


                
<section class="author-card">
        <img class="author-profile-image" src="/content/images/size/w100/2019/03/IMG_20160610_153242--2-.jpg" alt="Phil Best">
    <section class="author-card-content">
        <h4 class="author-card-name"><a href="/author/phil/">Phil Best</a></h4>
            <p>I'm a freelance developer, mostly working in web development. I also help create course content for Teclado!</p>
    </section>
</section>
<div class="post-full-footer-right">
    <a class="author-card-button" href="/author/phil/">Read More</a>
</div>


            </footer>


        </article>

    </div>
</main>

<aside class="read-next outer">
    <div class="inner">
        <div class="read-next-feed">
            <article class="read-next-card">
                <header class="read-next-card-header">
                    <h3 class="read-next-card-header-title"><a href="/tag/learn-python-programming/">Learn Python Programming</a></h3>
                </header>
                <div class="read-next-card-content">
                    <ul>
                        <li><a href="/python-snippet-13-zip/">Python Snippet 13: zip</a>
                            <div class="teclado-arrow">-&gt;</div>
                        </li>
                        <li><a href="/how-to-start-learning-python/">How to Start Learning Python</a>
                            <div class="teclado-arrow">-&gt;</div>
                        </li>
                        <li><a href="/python-snippet-12-a-closer-look-at-print/">Python Snippet 12: A Closer Look at Print</a>
                            <div class="teclado-arrow">-&gt;</div>
                        </li>
                    </ul>
                </div>
                <footer class="read-next-card-footer">
                    <a href="/tag/learn-python-programming/"><span class="teclado-arrow">-&gt;</span>
                        See all 57 posts</a>
                </footer>
            </article>

            <article class="post-card post tag-learn-python-programming ">

    <a class="post-card-image-link" href="/creating-a-new-sequence-type-in-python-part-1/">
        <img class="post-card-image" srcset="/content/images/size/w600/2019/04/max-nelson-492729-unsplash.jpg 600w,
                    /content/images/size/w1000/2019/04/max-nelson-492729-unsplash.jpg 1000w,
                    /content/images/size/w2000/2019/04/max-nelson-492729-unsplash.jpg 2000w" sizes="(max-width: 1000px) 400px, 700px" src="/content/images/size/w600/2019/04/max-nelson-492729-unsplash.jpg" alt="Creating a New Sequence Type in Python - Part 1">
    </a>

    <div class="post-card-content">

        <a class="post-card-content-link" href="/creating-a-new-sequence-type-in-python-part-1/">

            <header class="post-card-header">
                    <span class="post-card-tags">Learn Python Programming</span>
                <h2 class="post-card-title">Creating a New Sequence Type in Python - Part 1</h2>
            </header>

            <section class="post-card-excerpt">
                <p>Learn to exploit the power of Python's magic methods by creating a new sequence type from scratch!</p>
            </section>

        </a>

        <footer class="post-card-meta">

            <ul class="author-list">
                <div class="author-avatar-name">
                            <a href="/author/phil/" class="static-avatar">
                                <img class="author-profile-image" src="/content/images/size/w100/2019/03/IMG_20160610_153242--2-.jpg">
                            </a>
                    <div class="post-info">
                        <span class="author-name"><a href="/author/phil/">Phil Best</a></span>
                        <div class="post-metadata">
                            <span class="reading-time">9 min read</span> · 
                            <time class="post-full-meta-date" datetime="2019-04-19">Apr 19</time>
                        </div>
                    </div>
                </div>
        </ul></footer>

    </div>

</article>

            

            <script>
                var posts = document.querySelectorAll(".read-next-feed .post-card.post");
                console.log(posts);
                if (posts.length == 2) {
                    posts[1].remove();
                }
            </script>
        </div>
    </div>
</aside>

<div class="floating-header floating-active">
    <div class="floating-header-logo">
        <a class="site-nav-logo" href="https://blog.tecladocode.com"><img src="/content/images/2019/05/logo-white.svg" alt="The Teclado Blog"></a>
    </div>
    <div class="floating-header-title">Python Slices Part 2: The Deep Cut</div>
    <div class="floating-header-share">
        <div class="floating-header-share-label">Share this</div>
        <a class="floating-header-share-tw" href="https://twitter.com/share?text=Python%20Slices%20Part%202%3A%20The%20Deep%20Cut&amp;url=https://blog.tecladocode.com/python-slices-part-2/" onclick="window.open(this.href, 'share-twitter', 'width=550,height=235');return false;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M30.063 7.313c-.813 1.125-1.75 2.125-2.875 2.938v.75c0 1.563-.188 3.125-.688 4.625a15.088 15.088 0 0 1-2.063 4.438c-.875 1.438-2 2.688-3.25 3.813a15.015 15.015 0 0 1-4.625 2.563c-1.813.688-3.75 1-5.75 1-3.25 0-6.188-.875-8.875-2.625.438.063.875.125 1.375.125 2.688 0 5.063-.875 7.188-2.5-1.25 0-2.375-.375-3.375-1.125s-1.688-1.688-2.063-2.875c.438.063.813.125 1.125.125.5 0 1-.063 1.5-.25-1.313-.25-2.438-.938-3.313-1.938a5.673 5.673 0 0 1-1.313-3.688v-.063c.813.438 1.688.688 2.625.688a5.228 5.228 0 0 1-1.875-2c-.5-.875-.688-1.813-.688-2.75 0-1.063.25-2.063.75-2.938 1.438 1.75 3.188 3.188 5.25 4.25s4.313 1.688 6.688 1.813a5.579 5.579 0 0 1 1.5-5.438c1.125-1.125 2.5-1.688 4.125-1.688s3.063.625 4.188 1.813a11.48 11.48 0 0 0 3.688-1.375c-.438 1.375-1.313 2.438-2.563 3.188 1.125-.125 2.188-.438 3.313-.875z"></path></svg>
        </a>
        <a class="floating-header-share-fb" href="https://www.facebook.com/sharer/sharer.php?u=https://blog.tecladocode.com/python-slices-part-2/" onclick="window.open(this.href, 'share-facebook','width=580,height=296');return false;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M19 6h5V0h-5c-3.86 0-7 3.14-7 7v3H8v6h4v16h6V16h5l1-6h-6V7c0-.542.458-1 1-1z"></path></svg>
        </a>
    </div>
    <progress id="reading-progress" class="progress" value="2600" max="6948">
        <div class="progress-container">
            <span class="progress-bar"></span>
        </div>
    </progress>
</div>



<div class="post-footer form-container">
    <div class="signup-form-container">
        <form action="https://www.getdrip.com/forms/195051776/submissions" method="post" data-drip-embedded-form="195051776" data-drip-id="195051776">
            <h3 data-drip-attribute="headline">Like what you see? Enter your  e-mail to hear when new posts come out!</h3>
            <div class="fields-container">
                <div data-drip-attribute="description"></div>
                <div>
                    <label for="drip-email" class="field-label">E-mail
                        <input type="email" id="drip-email" class="input-field" name="fields[email]" value="" placeholder="E-mail*">
                    </label>
                </div>
                <div>
                    <label for="drip-full-name" class="field-label">Name
                        <input type="text" id="drip-full-name" class="input-field" name="fields[full_name]" value="" placeholder="Name*">
                    </label>
                </div>
                <div class="newsletter-terms">
                    Receive our newsletter and get notified about new posts we publish on the site, as well as
                    occasional
                    special offers.
                </div>
                <div style="display: none;" aria-hidden="true">
                    <label for="website">Website
                        <input type="text" id="website" name="website" tabindex="-1" autocomplete="false" value="">
                    </label>
                </div>
                <div>
                    <input type="submit" class="submit-button" value="Sign Up" data-drip-attribute="sign-up-button">
                </div>
            </div>
        <input type="hidden" name="time_zone" value="Asia/Jerusalem"><input type="hidden" name="url" value="https://blog.tecladocode.com/python-slices-part-2/"><input type="hidden" name="page_title" value="Python Slices Part 2: The Deep Cut"></form>
    </div>
</div>

        <footer class="site-footer outer">
            <div class="site-footer-content inner">
                <section class="copyright"><a href="https://blog.tecladocode.com">The Teclado Blog</a> © 2019
                </section>
                <nav class="site-footer-nav">
                    <a class="social-link" href="/privacypolicy" title="Privacy Policy" target="_blank" rel="noopener">Privacy Policy</a>
                    <a class="social-link social-link-yt" href="https://www.youtube.com/channel/UCINg1S61mpN7dZW8vR2ikCw" title="YouTube" target="_blank" rel="noopener"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"></path></svg></a>
                    <a class="social-link social-link-tw" href="https://twitter.com/tecladocode" title="Twitter" target="_blank" rel="noopener"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M30.063 7.313c-.813 1.125-1.75 2.125-2.875 2.938v.75c0 1.563-.188 3.125-.688 4.625a15.088 15.088 0 0 1-2.063 4.438c-.875 1.438-2 2.688-3.25 3.813a15.015 15.015 0 0 1-4.625 2.563c-1.813.688-3.75 1-5.75 1-3.25 0-6.188-.875-8.875-2.625.438.063.875.125 1.375.125 2.688 0 5.063-.875 7.188-2.5-1.25 0-2.375-.375-3.375-1.125s-1.688-1.688-2.063-2.875c.438.063.813.125 1.125.125.5 0 1-.063 1.5-.25-1.313-.25-2.438-.938-3.313-1.938a5.673 5.673 0 0 1-1.313-3.688v-.063c.813.438 1.688.688 2.625.688a5.228 5.228 0 0 1-1.875-2c-.5-.875-.688-1.813-.688-2.75 0-1.063.25-2.063.75-2.938 1.438 1.75 3.188 3.188 5.25 4.25s4.313 1.688 6.688 1.813a5.579 5.579 0 0 1 1.5-5.438c1.125-1.125 2.5-1.688 4.125-1.688s3.063.625 4.188 1.813a11.48 11.48 0 0 0 3.688-1.375c-.438 1.375-1.313 2.438-2.563 3.188 1.125-.125 2.188-.438 3.313-.875z"></path></svg>
</a>
                </nav>
            </div>
        </footer>

    </div>


    <script>
        var images = document.querySelectorAll('.kg-gallery-image img');
        images.forEach(function (image) {
            var container = image.closest('.kg-gallery-image');
            var width = image.attributes.width.value;
            var height = image.attributes.height.value;
            var ratio = width / height;
            container.style.flex = ratio + ' 1 0%';
        })
    </script>


    <script src="https://code.jquery.com/jquery-3.2.1.min.js" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=" crossorigin="anonymous">
        </script>
    <script type="text/javascript" src="/assets/built/jquery.fitvids.js?v=79f9761232"></script>


    <script>

    // NOTE: Scroll performance is poor in Safari
    // - this appears to be due to the events firing much more slowly in Safari.
    //   Dropping the scroll event and using only a raf loop results in smoother
    //   scrolling but continuous processing even when not scrolling
    $(document).ready(function () {
        // Start fitVids
        var $postContent = $(".post-full-content");
        $postContent.fitVids();
        // End fitVids

        var progressBar = document.querySelector('#reading-progress');
        var header = document.querySelector('.floating-header');
        var title = document.querySelector('.site-header-content');

        var lastScrollY = window.scrollY;
        var lastWindowHeight = window.innerHeight;
        var lastDocumentHeight = $(document).height();
        var ticking = false;

        function onScroll() {
            lastScrollY = window.scrollY;
            requestTick();
        }

        function onResize() {
            lastWindowHeight = window.innerHeight;
            lastDocumentHeight = $(document).height();
            requestTick();
        }

        function requestTick() {
            if (!ticking) {
                requestAnimationFrame(update);
            }
            ticking = true;
        }

        function update() {
            var trigger = title.getBoundingClientRect().top + window.scrollY;
            var triggerOffset = title.offsetHeight + 35;
            var progressMax = lastDocumentHeight - lastWindowHeight;

            // show/hide floating header
            if (lastScrollY >= trigger + triggerOffset) {
                header.classList.add('floating-active');
            } else {
                header.classList.remove('floating-active');
            }

            progressBar.setAttribute('max', progressMax);
            progressBar.setAttribute('value', lastScrollY);

            ticking = false;
        }

        window.addEventListener('scroll', onScroll, { passive: true });
        window.addEventListener('resize', onResize, false);

        update();

    });
</script>


    <div id="amzn-assoc-ad-4365f2d6-4bcf-4f48-9f94-0d82aa9de739"></div><script async="" src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US&amp;adInstanceId=4365f2d6-4bcf-4f48-9f94-0d82aa9de739"></script>
<!-- Drip -->
<script type="text/javascript">
  var _dcq = _dcq || [];
  var _dcs = _dcs || {};
  _dcs.account = '5640782';

  (function() {
    var dc = document.createElement('script');
    dc.type = 'text/javascript'; dc.async = true;
    dc.src = '//tag.getdrip.com/5640782.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(dc, s);
  })();
</script>
<!-- end Drip -->
    <script src="/assets/built/prism.js?v=79f9761232"></script>


<div class="drip-tab-container">
  <div id="drip-121349" class="drip-tab bottom right no-image">
    <div id="drip-header-121349" class="drip-header">
      <a href="#" id="drip-toggle-121349" class="drip-toggle">
        <h2 id="drip-teaser-121349">Enjoying this post?</h2>
        <span id="drip-tab-up-121349" class="drip-arrow up">
          <svg width="12px" height="8px" viewBox="1362 659 12 8" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            <polygon id="right_angle" stroke="none" fill="#FFFFFF" fill-rule="evenodd" transform="translate(1368.000000, 662.703125) rotate(-90.000000) translate(-1368.000000, -662.703125) " points="1364.29688 667.296875 1368.89062 662.703125 1364.29688 658.109375 1365.70312 656.703125 1371.70312 662.703125 1365.70312 668.703125"></polygon>
          </svg>
        </span>
        <span id="drip-tab-down-121349" class="drip-arrow down" style="display: none"></span>
      </a>
    </div>
    <div id="drip-content-121349" class="drip-content drip-clearfix" style="height: auto; bottom: -645px;">
      <a id="drip-close-121349" class="drip-close">
        <svg width="12px" height="12px" viewBox="630 19 12 12" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
          <polygon id="x" stroke="none" fill="#A8ACB9" fill-rule="evenodd" points="641.376687 30.1740899 636.49366 24.436669 641.095466 19 639.510399 19 635.701126 23.6038176 631.866288 19 630.281221 19 634.883028 24.436669 630 30.1740899 631.585067 30.1740899 635.701126 25.2463857 639.791621 30.1740899"></polygon>
        </svg>
      </a>

      <div id="drip-form-panel-121349" class="drip-panel drip-clearfix" style="display: block;">
        

        <div class="drip-form-main">
          <h3 id="drip-content-header-121349">Enjoying this post?</h3>
          
            <div id="drip-scroll-121349" class="drip-scroll">
          
            <div class="drip-description">You should give our e-mail list a try. We'll send you great new content a couple times per month, right when it comes out.</div>
            <form id="drip-form-121349">
              <div style="display: none">
                <input type="hidden" name="form_id" value="121349">
              </div>
              <dl class="">
                
                  
                    <dt>Email Address</dt>
                    <dd>
                      
                        <input type="email" name="fields[email]" value="" placeholder="" class="drip-text-field">
                        <div id="drip-errors-for-email-121349" class="drip-errors"></div>
                      
                    </dd>
                  
                
                  
                    <dt>First Name</dt>
                    <dd>
                      
                        <input type="text" name="fields[first_name]" value="" placeholder="" class="drip-text-field">
                        <div id="drip-errors-for-custom-fields-first-name-121349" class="drip-errors"></div>
                      
                    </dd>
                  
                
                
                <div style="display: none;" aria-hidden="true">
                  <dt for="website">Website</dt>
                  <dd>
                    <input type="text" id="website" name="website" placeholder="Website" class="drip-text-field" tabindex="-1" autocomplete="false" value="">
                  </dd>
                </div>
              </dl>
              <div class="form-controls">
                <input type="submit" name="submit" value="Sign Up" id="drip-submit-121349" class="drip-submit-button">
              </div>
            </form>
          </div>
        </div>
      </div>

      <div id="drip-success-panel-121349" class="drip-success drip-panel drip-clearfix" style="display: none">
        <h3>Thank you for signing up!</h3>
        <p class="drip-description drip-post-submission">Please check your email and click the link provided to confirm your subscription.</p>
      </div>

      
    </div>
  </div>
</div></body></html>
'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


tag = simple_soup.find('p', {'class': 'drip-description drip-post-submission'})

# l = []
# l = [i.string for i in tag]
# print(l)
print(tag.string)
