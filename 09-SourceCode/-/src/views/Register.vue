<template>
  <div id="building">
  <div class="register-container">
    <div style="text-align: center;height: 50px">
      注册
    </div>
    <el-form :model="registerData" label-width="80px">
      <el-form-item label="用户名">
        <el-input v-model="username" placeholder="请输入用户名"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input type="password" v-model="password" placeholder="请输入密码"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="registerUser" style="margin-left: 100px;width: 70px;">注册</el-button>
        <el-button type="primary" @click="registerMa" style="margin-left: 100px;width: 70px;margin-top: 2px">注册管理员</el-button>
      </el-form-item>
      <p class="login-link" @click="gotologin" style="text-align: center;height: 50px">已有账号？点击返回</p>
    </el-form>
  </div>
  </div>
</template>

<script>
import { ElForm, ElFormItem, ElInput, ElButton } from 'element-plus';
import { reactive, toRefs } from "vue";
import { useRouter } from "vue-router";
import { ElMessage } from "element-plus";
import { registercommon, registerManager } from "@/api/user";
export default {
  name: 'RegisterPage',
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
    });

    const registerUser = async () => {
      if (!state.username) {
        ElMessage.error("用户名不能为空！");
        return;
      }
      if (!state.password) {
        ElMessage.error("密码不能为空！");
        return;
      }
       const {data} = await registercommon(state.username, state.password);
      if(data.result == "0"){
        ElMessage.error("用户名已存在");
      }
      if(data.result != "0"){
        ElMessage.success("注册成功");
        router.push({ path: "/login" });
      }
    };
    const registerMa = async () => {
      if (!state.username) {
        ElMessage.error("用户名不能为空！");
        return;
      }
      if (!state.password) {
        ElMessage.error("密码不能为空！");
        return;
      }
      const {data} = await registerManager(state.username, state.password);
      if(data.result == "0"){
        ElMessage.error("用户名已存在");
      }
      if(data.result != "0"){
        ElMessage.success("注册成功");
        router.push({ path: "/login" });
      }
    };
    const gotologin = () => {
      router.push({ path: "/login" });
    };
    return {
      ...toRefs(state),
      registerUser,
      gotologin,
      registerMa,
    };
  },
};
</script>

<style scoped>
.register-container {
   width: 400px;
  height: 300px;
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
