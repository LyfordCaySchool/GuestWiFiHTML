
function addPlaceHolders(){
	if(checkPlaceHolders()){
	     initPlaceHolders();
	}
}

function checkPlaceHolders(){
		if('placeholder' in document.createElement('input')){ 
			return false;
		}
		return true;
}


function initPlaceHolders(){
	function target (e){
		var e=e||window.event;
		return e.target||e.srcElement;
	};
	function _getEmptyHintEl(el){
		var hintEl=el.hintEl;
		return hintEl && g(hintEl);
	};
	function blurFn(e){
		var el=target(e);
		if(!el || el.tagName !='INPUT' && el.tagName !='TEXTAREA') return;
		var	emptyHintEl=el.__emptyHintEl;
		if(emptyHintEl){
			if(el.value) 
				emptyHintEl.style.display='none';
			else 
				emptyHintEl.style.display='';
		
		}
	};
	function focusFn(e){
		var el=target(e);
		if(!el || el.tagName !='INPUT' && el.tagName !='TEXTAREA') return;
		var emptyHintEl=el.__emptyHintEl;
		if(emptyHintEl){
			emptyHintEl.style.display='none';
		}
	};
	if(document.addEventListener){
		document.addEventListener('focus',focusFn, true);
		document.addEventListener('blur', blurFn, true);
	}
	else{
		document.attachEvent('onfocusin',focusFn);
		document.attachEvent('onfocusout',blurFn);
	}

	var elss=[document.getElementsByTagName('input'),document.getElementsByTagName('textarea')];
	for(var n=0;n<2;n++){
		var els=elss[n];
		for(var i =0;i<els.length;i++){
			var el=els[i];
			var placeholder=el.getAttribute('placeholder'),
				emptyHintEl=el.__emptyHintEl;
			if(placeholder && !emptyHintEl){
				emptyHintEl=document.createElement('span');
				emptyHintEl.innerHTML=placeholder;
				emptyHintEl.className='placeholder';
				emptyHintEl.onclick=function (el){return function(){try{el.focus();}catch(ex){}}}(el);
				if(el.value) emptyHintEl.style.display='none';
				el.parentNode.insertBefore(emptyHintEl,el);
				el.__emptyHintEl=emptyHintEl;
			}
		}
	}
}

var validateSubmit = function(formIndex){
	    var elss=[formIndex.getElementsByTagName('input'),formIndex.getElementsByTagName('textarea')];
		for(var n=0;n<2;n++){
			var els=elss[n];
			for(var i =0;i<els.length;i++){
				var el=els[i];
				var required=el.getAttribute('required');
				if(required != null){
						if(el.value == null || el.value == '' ){
							var message = 'Please fill out this field '+el.getAttribute('placeholder');
							reportFieldError(el, message);
							return false;
						}
				}
			}
		}  
}

fieldErrorIds = new Array();
var fieldErrorTimeoutId;

function reportFieldError(element, message) {
	clearTimeout(fieldErrorTimeoutId);
	var feId = "fe_" + element.id;
	var fe = document.getElementById(feId);
	if (fe == null) {
		var td = document.createElement("td");
		td.className = 'noteError';
		td.setAttribute("id", "text" + feId);
		td.appendChild(document.createTextNode(message));
		var tr = document.createElement("tr");
		tr.appendChild(td);
		var tbody = document.createElement("tbody");
		tbody.appendChild(tr);
		var table = document.createElement("table");
		table.border ="0";
		table.cellSpacing = "0";
		table.cellPadding = "0";
		table.appendChild(tbody);
		var div = document.createElement("div");
		div.setAttribute("id", feId);
		div.style.display = "none";
		div.appendChild(table);
		tr = document.createElement("tr");
		td = document.createElement("td");
		td.appendChild(div);
		tr.appendChild(td);
		var row = element.parentNode.parentNode;
		table = row.parentNode;
		table.insertBefore(tr, row);
	} else {
		var td = document.getElementById("text" + feId);
		td.removeChild(td.firstChild);
		td.appendChild(document.createTextNode(message));
	}
	if (vectorContains(fieldErrorIds, feId)) {
	} else {
		fieldErrorIds.push(feId);
		
		document.getElementById(feId).style.display = "";
	}
	delayHideFieldError(2);
}


function delayHideFieldError(seconds) {
	fieldErrorTimeoutId = setTimeout("hideFieldError()", seconds * 1000);  // seconds
}


function hideFieldError() {
	for (var i = 0; i < fieldErrorIds.length; i++) {
		document.getElementById(fieldErrorIds[i]).style.display = "none";
	}
	fieldErrorIds = new Array();
}

function vectorContains(vector, element) {
	for (var i = 0; i < vector.length; i++) {
		if (vector[i] == element) {
			return true;
		}
	}
	return false;
}