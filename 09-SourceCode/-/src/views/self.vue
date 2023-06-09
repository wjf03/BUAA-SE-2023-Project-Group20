<template>
	<div class="background">
		<div>
			<div class="header">
				<div class="section_inner">
					<div class="section_inner_wrap">
						<h1 class="market_title" style="color:white;">
							怡心阅读
						</h1>
						<div class="section_inner_right">
							<ul class="ul_top">
								<li class="li_nav_top">
									<router-link :to="getHomeRoute()" class="top_nav_link">首页</router-link>
								</li>
								<li class="li_nav_top">
									<router-link :to="getlibrary()" class="top_nav_link">进入书城</router-link>
								</li>
							</ul>
							<div class="book_search">
								<input type="text" v-model="booksearch" id="booksearch" name="booksearch"
									placeholder="请输入书名" autocomplete="off">
								<i class="el-icon-search" @click="search()"></i>
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
				<div  style="display: inline-block;;float: left;">
					<img class="avatar" style="margin-top: 10px;margin-right: 5px; float: left;"
						src="../assets/yomu.jpg" alt="">
					<div style="color:white;float: left;margin-left: 5px;">
						{{nickName}}
					</div>
				</div>
			</div>
			<div class="container">
				<router-view v-on:loginstate="loginstate"></router-view>
			</div>
		</div>
		<div class="change">
			 <h2  style="color:white;" class="title">个人信息修改</h2>
			
					  <img
						:src=" man"
						class="avatar"
					  />
				   
		<el-form label-width="100px">
			<el-form-item >
			<span style="color: white">用户类型:  {{type}}</span>
			</el-form-item>
		  <el-form-item >
			<span style="color: white">用户名:</span>
			<el-input v-model="nickName" class="input-width"></el-input>
		  </el-form-item>
		<el-form-item>
			<span style="color: white">性别:</span>
			<el-radio-group v-model="gender">
			  <el-radio label="male" class="gender-radio" style="color:white;">男</el-radio>
	  <el-radio label="female" class="gender-radio" style="color:white;">女</el-radio>
			</el-radio-group>
		  </el-form-item>
		  <el-form-item>
			<el-button type="primary" @click="saveChanges" class="save">保存</el-button>
		  </el-form-item>
		<el-form-item>
			<el-button type="primary" @click="gotocollection" class="collect">我的收藏</el-button>
		  </el-form-item>
		</el-form>
		</div>
	</div>
	</template>
	<script>
	import man from "@/assets/yomu.jpg";
	import { reactive, toRefs, onMounted } from "vue";
	import { useRoute, useRouter} from "vue-router";
	import { getUser,modifyUser } from "@/api/user";
	import { ElMessage } from 'element-plus';
		export default {
			name: "selfData",
		setup() {
	
		const state = reactive({
		  type: "",
		  nickName: "",
		gender: "",
		id: "",
		if: "",
		});
		onMounted(async () => {
			const route = useRoute();
		state.id = route.query.id;
		  const { data } = await getUser(state.id);
		  state.nickName = data.result.name;
		state.if = data.result.ifManager;
		sessionStorage.setItem("userid", state.id);
		if(state.if == "1"){
			state.type = "管理员";
		}
		if(state.if == "0"){
			state.type = "普通用户"
		}
		});
		const router = useRouter();
		const saveChanges = async () => {
			if(state.gender == "male"){
				const { data } = await modifyUser(state.id,state.nickName,0);
				if(data.result=="0"){
					ElMessage.error(data.message);
				}
			}
			if(state.gender == "female"){
				const { data } = await modifyUser(state.id,state.nickName,1);
				if(data.result=="0"){
					ElMessage.error(data.message);
				}
			}
		};
		const getHomeRoute = () => {
		  return {
			path: "/home",
			query: { id: state.id },
		  };
		};
		const getlibrary = () => {
		  return {
			path: "/library",
			query: { id: state.id, isLibrary: 1 },
		  };
		};
		const gotocollection = () => {
			router.push({path: "/libraryown", query:{id:state.id, isLibrary: 0}})
		}
		return {
		  ...toRefs(state),
		  man,
		saveChanges,
		getHomeRoute,
		getlibrary,
		gotocollection,
		};
	  },
	  }
	</script>
	
	<style scoped>
	.gender-radio {
	  margin-left: 50px;
	}
	.change .avatar {
		position: relative;
		border-radius: 50%;
		top: 10px;
		left: 850px;
	  width: 178px;
	  height: 178px;
	  display: block;
	}
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
		.change{
			margin-top: 50px;
			text-align: center;
			width: 100%;
			height: 100%;
		}
		.input-width {
			text-align: center;
	  width: 300px; /* 设置输入框宽度 */
	}
	
	.el-form-item {
		margin-left: 700px;
		text-align: center;
		margin-top:  50px;
	  margin-bottom: 20px; /* 设置组件之间的间隔 */
	}
	.save{
		width:100px;
		margin-left: 100px;
		margin-top:  -20px;
	}
	.collect{
		width:100px;
		margin-left: 100px;
		margin-top:  -20px;
	}
		.background{
	  background:url("../assets/BJ3.jpg");
	  width:100%;
	  height:100%;
	  position:fixed;
	  background-size:100% 100%;
	  z-index: 1;}
	  .title{
		position: relative;
		left: 0px;
	  }
	</style>