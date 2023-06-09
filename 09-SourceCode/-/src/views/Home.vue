<template>
	<div class="background">
	<div class="headzz">
		<div class="header">
			<div class="section_inner">
				<div class="section_inner_wrap">
					<h1 class="market_title" style="color:white;">
						怡心阅读
					</h1>
					<div class="section_inner_right">
						<ul class="ul_top">
							<li class="li_nav_top">
								<router-link to="/home" class="top_nav_link">首页</router-link>
							</li>
							<li class="li_nav_top">
								<router-link :to="getlibrary()" class="top_nav_link">进入书城</router-link>
							</li>
						</ul>
						<div class="book_search">
							<input type="text" v-model="keyword" id="booksearch" @keydown.enter="handleKeyDown" name="booksearch"
								placeholder="请输入书名" autocomplete="off">
						</div>
						<div>
						</div>
					</div>
					<div style="cursor: pointer;">

					</div>
				</div>
			</div>
		</div>
		<div style="float: right;margin-top: -68px;margin-right: 40px;line-height: 60px;">
			<div @click="selfmessage()" style="display: block;float: left;">
				<img class="avatar" style="margin-top: 10px;margin-right: 5px; float: left;"
					src="../assets/yomu.jpg" alt="">
				<div style="color:white;float: left;margin-left: 5px;">
					{{name}}
				</div>
			</div>
			<a @click="exit()" style="margin-left: 18px; margin-top: 18px; cursor:pointer;color: #9e9e9e;">退出</a>
		</div>
		<div class="container">
			<router-view v-on:loginstate="loginstate"></router-view>
		</div>
	</div>
	<div class="mainscene">
    <div class="welcome">
        <h1 style="color:white;">
            欢迎来到怡心阅读
        </h1>
        <h1 style="color:white;">
            根据您的兴趣,我们为您推荐了如下书籍
        </h1>
    </div>
    <div class="book" style="height: 100%;">
		<div>
			<li class="bookhighscore">
				近期高分
			</li>
			<div class="book1">
				<div class="book1image" @click="gotobook1"></div>
				<div class="book1inter">
					<div class="book1desc">
					<span style="color: white;">
						李云龙是一个叱咤风云、百战沙场的职业军人，是一个一生都在血与火中搏斗的名将。他的人生信条是：面对强大的对手，明知不敌，也要毅然亮剑，即使倒下，也要成为一座山、一道岭。在战争与和平的时空转换中，他的命运注定要充满悲欢离合—无论是政治生涯还是婚姻、爱情
					</span>
					</div>
				<div class="book1comment">
					<span class="other">
						阅读次数: 2489          评论数:6666
						</span>
						</div>
						</div>
			</div>
			<li class="collection">
				您的收藏
			</li>
			<div class="book2">
				<div class="book2image" @click="gotobook2"></div>
				<div class="book2inter">
					<div class="book2desc">
					<span style="color: white;">
						本书描写傲慢的单身青年达西与偏见的二小姐伊丽莎白、富裕的单身贵族彬格莱与贤淑的大小姐吉英之间的感情纠葛，充分表达了作者本人的婚姻观，强调经济利益对恋爱和婚姻的影响。小说情节富有喜剧性，语言机智幽默，是奥斯丁小说中最受欢迎的一部，并被多次改编成电影和电视剧。
					</span>
					</div>
				<div class="book2comment">
					<span class="other">
						阅读次数: 1645          评论数:4755
						</span>
						</div>
				</div>
			</div>
			<li class="haread">
				最近读过
			</li>
			<div class="book3">
				<div class="book3image" @click="gotobook3"></div>
				<div class="book3inter">
					<div class="book3desc">
					<span style="color: white;">
						故事发生于1920至1940年代。主角方鸿渐是个从中国南方乡绅家庭走出的青年人，迫于家庭压力与同乡周家女子订亲。但在其大学期间，周氏患病早亡。准岳父周先生被方所写的唁电感动，资助他出国求学。
到达上海后，方鸿渐在准岳父周先生开办的银行任职。此时，他获得了同学苏文纨的青睐，并与苏的表妹唐晓芙一见钟情，整日周旋于苏、唐二人之间，同时，结识了追求苏文纨的赵辛楣。方鸿渐*终与苏、唐二人感情终结，苏嫁与诗人曹元朗，而赵辛楣也明白方鸿渐并非其情敌，从此与方惺惺相惜。因为诸多原因，方鸿渐逐渐与周家不和
					</span>
					</div>
				<div class="book3comment">
					<span class="other">
						阅读次数: 3089          评论数:6503
						</span>
						</div>
				</div>
			</div>
		</div>
    </div>
	</div>
	</div>
</template>

<script>
import man from "@/assets/yomu.jpg";
	import { reactive, toRefs, onMounted } from "vue";
import { useRouter,useRoute } from "vue-router";
import { getUser } from "@/api/user";
	export default {
        name: "homePage",
	setup() {
		
    const state = reactive({
      keyword: "",
      name: "",
      type: "",
	id: "",
	book1title:"",
	book1desc:"",
	book1type:"",
	book1auth:"",
	book2title:"",
	book2desc:"",
	book2type:"",
	book2auth:"",
	book3title:"",
	book3desc:"",
	book3type:"",
	book3auth:"",
    });
	
	onMounted(async () => {
		if(sessionStorage.getItem("key")){
		state.id=sessionStorage.getItem("key");
	}
	else{
		const route = useRoute();
    state.id = route.query.id;
	}
      const { data } = await getUser(state.id);
      state.name = data.result.name;
	state.type = data.result.ifManager;
	console.log(data);
    });
	const router = useRouter();
    const searchByK = () => {
      /* router.push({ path: "/bookclass", query: { key: state.keyword } });
      context.emit("eventSerch", state.keyword); */
    };
	const gotobook = () => {
      router.push({ path: "/book" });
    };
	
    const exit = () => {
	router.push({path: "/login"});
    };
	const handleKeyDown = (event) => {
      if (event.key === "Enter") {
        searchByK();
      }
    };
	const selfmessage = () => {
		router.push({path: "/self", query:{id:state.id}})
	}
	const getlibrary = () => {
      return {
        path: "/library",
        query: { id: state.id, isLibrary: 1 },
      };
    };
    return {
      ...toRefs(state),
      searchByK,
      exit,
	selfmessage,
	handleKeyDown,
	gotobook,
	getlibrary,
	man,
    };
  },
	}
</script>

<style scoped>
	*,
	body,
	ul,
	li,
	h1,
	h2,
	h3,
	h4,
	h5 {
		margin: 0;
		padding: 0;
	}

	a {
		text-decoration: none;
		outline: none;
		color: #9e9e9e;
		font-family: "Microsoft Yahei", arial, sans-serif;
	}

	i {
		font-style: normal;
		font-weight: normal;
	}

	body {
		color: #9e9e9e;
		font: 12px/20px "Microsoft Yahei", arial, sans-serif;
		background: #f0f0f0;
		font-weight: normal;
		max-width: 100%;
		min-width: 100%;
	}

	ul,
	li {
		overflow: hidden;
	}

	.header {
		width: 100%;
		height: 68px;
		min-width: 100%;
		/* position: fixed; */
	}


	.section_inner_wrap {
		width: 1100px;
		height: 68px;
		line-height: 68px;
		margin: 0 auto;
		padding: 0 2px;
	}

	.section_inner_wrap h1 {
		float: left;
		height: 68px;
		font-style: normal;
		font-weight: normal;
	}

	.market_title {
		font-size: 24px;
	}

	.section_inner_right {
		float: right;
		height: 68px;
	}

	.ul_top {
		float: left;
		overflow: hidden;
	}

	.li_nav_top {
		position: relative;
		float: left;
		margin-left: 20px;
		list-style: none;
		border-bottom: 3px solid transparent;
		height: 50px;
		color: #9e9e9e;
		transition: 0.5s;
	}

	.li_nav_top:hover {
		border-bottom-color: #FF5858;
		color: #000;
	}

	.top_nav_link {
		display: block;
		padding: 0 20px;
		text-align: center;
		font-size: 18px;
	}

	.book_search {
		float: left;
		position: relative;
		/* margin-left: 300px; */
	}

	.book_search input {
		width: 200px;
		height: 30px;
		line-height: 30px;
		border: 1px solid #d2d2d2;
		border-radius: 50px;
		color: #9e9e9e;
		margin: 0 22px 0 20px;
		padding: 0 36px 0 12px;
		font-size: 15px;
		outline: none;
		background: none;
	}

	.book_search input:hover {
		border-color: chocolate;
	}

	.el-icon-search {
		width: 15px;
		height: 15px;
		cursor: pointer;
		position: absolute;
		right: 40px;
		top: 27px;
	}

	.login_register {
		float: left;
		position: relative;
	}

	.el-icon-user {
		margin-left: 15px;
		margin-right: 5px;
	}

	.login_register a:hover {
		color: #f60;
		transition: 0.3s;
	}

	.container {
		width: 100%;
		/* padding-top: 68px; */
	}

	.avatar {
		width: 40px;
		height: 40px;
		border-radius: 40px;
	}

	.regist-btn {
		margin-top: -59px;
		margin-left: 60px;
	}
    .welcome{
        margin-top: -0px;
        text-align: center;
        width: 100%;
        height: 80px;
		border-bottom: 1px solid gray;
    }
	.bookhighscore{
		font-size: 30px; /* 设置字体大小 */
	margin: 0px auto;
	top: 0px;
    font-weight: bold; /* 设置加粗 */
    color: red; /* 设置颜色为红色 */
	width: 200px;
	}
	.collection{
		font-size: 30px; /* 设置字体大小 */
	top: 200px;
	margin: 0px auto;
    font-weight: bold; /* 设置加粗 */
    color: red; /* 设置颜色为红色 */
	width: 200px;
	}
	.haread{
		font-size: 30px; /* 设置字体大小 */
	top: 400px;
	margin: 0px auto;
    font-weight: bold; /* 设置加粗 */
    color: red; /* 设置颜色为红色 */
	width: 200px;
	}
	.mainscene{
		width: 900px;
		height: 900px;
		margin: 0px auto;
		background-color: #333;
		opacity: 0.8;
	}
	.background{
  background:url("../assets/BJ3.jpg");
  width:100%;
  height:100%;
  position:fixed;
  background-size:100% 100%;
  z-index: 1;}
	.book1{
		width:100%;
		height:200px;
		margin-top:0px;
		border-bottom: 1px solid gray;
		border-top: 1px solid gray;
	}
	.book2{
		width:100%;
		height:200px;
		margin-top:0px;
		border-bottom: 1px solid gray;
		border-top: 1px solid gray;
	}
	.book3{
		width:100%;
		height:200px;
		margin-top:0px;
		border-bottom: 1px solid gray;
		border-top: 1px solid gray;
	}
	.book1image{
		left:0px;
		height:200px;
		width:225px;
		border-right: 1px solid gray;
		float: left;
		background-image: url(../assets/book4.jpg);
		background-size:100% 100%;
	}
	.book2image{
		left:0px;
		height:200px;
		width:225px;
		border-right: 1px solid gray;
		background-image: url(../assets/book5.jpg);
		background-size:100% 100%;
		float: left;
	}
	.book3image{
		left:0px;
		height:200px;
		width:225px;
		border-right: 1px solid gray;
		background-image: url(../assets/book6.jpg);
		background-size:100% 100%;
		float: left;
	}
	.book1inter{
		left: 226px;
		height: 200px;
		width: 674px;
		float: left;
	}
	.book2inter{
		left: 226px;
		height: 200px;
		width: 673px;
		float: left;
	}
	.book3inter{
		left: 226px;
		height: 200px;
		width: 674px;
		float: left;
	}
	.book1comment{
		height: 20px;
	}
	.book1desc{
		height: 180px;
	}
	.book2comment{
		height: 20px;
	}
	.book2desc{
		height: 180px;
	}
	.book3comment{
		height: 20px;
	}
	.book3desc{
		height: 180px;
	}
	.other{
		bottom: 0;
		position: relative;
		color: white;
	}
	.book1title{
		margin-left:250px;
		color: white;
	}
	.book2title{
		margin-left:250px;
		color: white;
	}
	.book3title{
		margin-left:250px;
		color: white;
	}
</style>
