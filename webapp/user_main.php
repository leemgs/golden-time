<?php
require("./menu2.php");
session_start();
// if user does do log-in, go to login.html webapge.
if(!isset($_SESSION['id'])) {
    header('Location: ./user_login.php');
}
else{
    echo "<br>";
    echo "&nbsp;&nbsp;&nbsp;";
    echo "<b><font color=red>로그인을 성공하였습니다.</font></b><br>";
    echo "<br>";
    echo "<li>공장아이디: ".$_SESSION['id']."</li>";
    echo "<li>공장명: ".$_SESSION['name']."</li>";
    echo "<li>비밀번호: (<font color=white>".$_SESSION['password']."</font>)</li>";
    echo "<br><br>";
    echo "<img src=./images/login-success.gif width=300 border=0></img>";
    echo "<br><br>";
    echo "<a href=user_logout.php>로그아웃</a>";
}

?>
</body>
<?php
include('./information_footer.php');
?>
</html>
