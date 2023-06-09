<template>
  <div id="building">
  <div class="login-container">
    <div style="text-align: center;height: 50px">
      登录
    </div>
    <el-form :model="loginData" label-width="80px">
      <el-form-item label="用户名">
        <el-input v-model="username" placeholder="请输入用户名"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input type="password" v-model="password" placeholder="请输入密码"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="loginUser" class="loginbutton">登录</el-button>
      </el-form-item>
       <p class="register-link" @click="gotoregister" style="text-align: center;height: 50px">没有账号？点击注册</p>
    </el-form>
  </div>
  </div>
</template>

<script>
import { ElForm, ElFormItem, ElInput, ElButton, ElMessage } from 'element-plus';
import { reactive, toRefs } from "vue";
import { useRouter } from "vue-router";
import { login } from "@/api/user";
export default {
  name: 'LoginPage',
  components: {
    ElForm,
    ElFormItem,
    ElInput,
    ElButton,
  },
    setup() {
    const router = useRouter();

    const state = reactive({
      username: "",
      password: "",
      id: "",
    });

    const loginUser = async () => {
       if (!state.username) {
        ElMessage.error("用户名不能为空！");
        return;
      }
      if (!state.password) {
        ElMessage.error("密码不能为空！");
        return;
      }
      
      const { data } = await login(state.username, state.password);
      if(data.result == "0"){
        ElMessage.error(data.message);
      }
      if(data.result != "0"){
      state.id = data.result;
      ElMessage.success("登陆成功");
      router.push({ path: "/home", query:{id:state.id}});}
    };
    const gotoregister = () => {
      router.push({ path: "/register" });
    };


    return {
      ...toRefs(state),
      loginUser,
      gotoregister,
    };
  },
};
</script>

<style scoped>
.login-container {
  width: 400px;
  height: 250px;
  background: #e5e9f2;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  border-radius: 5px;
  padding-top: 40px;
  padding-right: 40px;
}
#building{
  background:url("../assets/BJ1.jpg");
  width:100%;
  height:100%;
  position:fixed;
  background-size:100% 100%;}

</style>
