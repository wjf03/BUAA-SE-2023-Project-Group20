<template>
  <div class="container" @click="bookInfo(bookId)" :title="name">
    <div style="display: flex; justify-content: center;">
      <img :src="require(`@/assets/${imgName}`)" alt="img" />
      <img v-if="isvip" src="@/assets/vip.png" style="position: absolute;" />
    </div>
    <p class="name">{{ name }}</p>
    <el-rate :modelValue="rate" disabled show-score score-template="{value}"></el-rate>
  </div>
</template>

<script>
import router from '@/router/router'
import { addPopularity } from '@/api/book'

export default {
  name: 'LittleBook',
  props: {
    bookId: Number,
    imgName: String, // 图片路径（'@/assets/'的相对路径）
    name: String, // 书名
    rate: Number, // 书的评分
    userId: Number
  },
  methods: {
    bookInfo () {
      this.$message.info('图书详情\nid: ' + this.bookId)
      addPopularity(this.bookId)
      router.push({ path: '/book/' + this.bookId, query: {userId: this.userId} })
    }
  }
}
</script>

<style scoped>
.container {
  width: 150px;
  height: 265px;
  border-width: 2px;
  border-color: lightgray;
  border-radius: 10px;
  border-style: solid;
  background-color: rgb(243, 255, 243);
}
.container:hover {
  box-shadow: 0 0 20px 8px rgb(235, 235, 235);
  cursor: pointer
}
img {
  width: 150px;
  height: 200px;
  border-width: 0px 0px 2px 0px;
  border-color: lightgray;
  border-radius: 10px 10px 0px 0px;
  border-style: solid;
}
.name {
  padding: 10px 15px 0px 15px;
  margin: 0px;
  width: 120px;
  overflow: hidden;
  text-overflow: ellipsis;
}
.el-rate {
  padding: 0px 12px;
}
/deep/ .el-rate__icon {
  font-size: 15px;
}
</style>
