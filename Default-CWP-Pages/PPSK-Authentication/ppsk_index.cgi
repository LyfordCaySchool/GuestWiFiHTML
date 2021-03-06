<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<meta name="viewport" content="width=device-width"/>  
	<title>Login</title>
	
	<script src="hm.cwp.util.js"></script>
	
	<script>
		if(document.addEventListener){
			window.addEventListener('load',addPlaceHolders,false);
		}else{
			window.attachEvent('onload',addPlaceHolders);
		} 
    </script>
	
	<style type="text/css">
	<!--
	body{
		background-color:#000000;
		background-image: url(default_hive.png);
		background-repeat: no-repeat;
		background-attachment:fixed;
		background-position: center;
		font-family:Helvetica, Arial, sans-serif;
		text-align:left;
		width:400px;
		margin:0 auto;
		font-size:14px;
		color: #FFFFFF;
		padding:0 20px;
	}
	
	a{
		color: #FFFFFF;
	}
	
	a:hover{
		color: #FFFFFF;
	}
	
	p{
		text-align:left;
		font-size:14px;
	}
	
	.note{
		width:200px;
		font-size:12px;
		line-height:14px;
		color: #FFFFFF;
	}
	
	h1{
		font-family:Century Gothic, Helvetica, Arial, sans-serif;
		font-size:30px;
		text-align:center;
		font-weight:300;
	}
	
	h2{
		color: #FFFFFF;
		line-height:14px;
	}
	
	h3{
		font-family:Century Gothic, Helvetica, Arial, sans-serif;
		color: #FFFFFF;
		text-align:center;
		font-size:24px;
		font-weight:300;
		margin-bottom:40px;
	}
		
	
	.req:after{
		color: #FFFFFF;
		font-size:16px;
		content:"*";
	}
	
	.login{
		width:380px;
		text-align:center;
		margin:0px auto 60px;
	}
	
	.login input{
		font-size:25px;
		margin-bottom:10px;
		width:300px;
		color: gray;
	}
	
	.login_button{
		float:right;
		background: url(login.png) no-repeat;
	    width: 125px;
		height: 40px;
	    border: 0px;
		margin-top:10px;
		cursor:pointer;
	
	}
	
	.register{
		width: 388px;
		text-align:center;
		margin-top:30px;
		margin:0 auto;
	}
	
	.register input{
		font-size:20px;
		margin-bottom:5px;
		color: gray;
		width:275px;
	}
	
	.reg_button{
		float:right;
		background: url(register.png) no-repeat 0px 5px;
		margin-top:5px;
	    width: 125px;
		height: 45px;
	    border: 0px;
		cursor:pointer;
	}
	
	.error{
		color: red;
		text-shadow: 0 0 3px #000;
		text-align:center;
		font-size:14px;
		line-height:14px;
	}
	
	span.placeholder {
		color:#808080;
		position:absolute;
		padding:3px;
		font-size:25px;
	}
	
	td.noteError {
		font-weight: bold;
		color: #FF0000;
		padding-left:30px;
		padding-bottom:5px;
	}
	-->
	</style>
</head>
<body>
<div style="height:600px;">
	<div style="height: 200px;"></div>
	<h1 id="h1Title">Secure Internet Portal</h1>
	<p><strong>If you have valid network credentials, please submit them below to receive your private preshared Key for secure network access. </strong></p>
	
	<form class="login" name="form2" action="ppsk_login.cgi" method="post" onsubmit="return validateSubmit(this);">
	<div>
		<table>
			<tr>
				<td>
					<div class="error" id="sipDeny">
						
		            </div>
		            <div class="error" id="addi_msg">
		            </div>
		            <div id="normal">
		                 <table>
		                 	<tr>
								<td>
							  		<div id="reason" class="error"/>
							  	</td>
							</tr>
							<tr>
							  	<td>
									<div id="replymsg" class="error"/>
							  	</td>
							</tr>
							<tr>
							  	<td>
									<div id="redir" class="error"/>
							  	</td>
							</tr>
		                 </table>
		            </div>
				</td>
			</tr>
		</table>
	</div>
	<table>
		<tr>
			<td>
				<input id="field12" type="text" name="username" maxlength=32 placeholder="username" required /><br />
			</td>
		</tr>
		<tr>
			<td>
				<input id="field22" type="password" name="password" maxlength=32 placeholder="password" required /><br />
			</td>
		</tr>
	</table>
	<div>
		<input style="width:140px;" type="submit" value=" " class="login_button" />
		<input name="checkbox" type="hidden" id="checkbox" value="checkbox" />
	</div>
	<!-- $PPSK_FLAG = LOGIN_ITEMS -->
	</form>
	
	<p style="float:right;"><img id="footImage" src="company_logo.png" style="width: 235px; height: 69px;"/></p>
</div>
</body>
</html>
