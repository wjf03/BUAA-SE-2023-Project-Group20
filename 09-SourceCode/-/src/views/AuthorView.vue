<template>
  <div style="background-color: aliceblue;">
    <div style="margin-left: 160px; margin-right: 160px;">
      <div style="background-color: lightblue; padding-top: 40px; padding-bottom: 10px;">
        <img class="author-image-box" src="@/assets/book.png" alt="img"/>
        <div style="display: inline-block; vertical-align: top;">
          <div class="author-name">{{ authorName }}</div>
          <el-scrollbar max-height="160px" style="margin: 10px 0px;">
            <div class="author-introduce">{{ introduce }}</div>
          </el-scrollbar>
        </div>
        <div v-if="userType == 'manager'" class="author-modify-container" @click="dialogFormVisible = true">
          <span>修改信息</span>
        </div>
      </div>
      <div style="text-align: center;">·····················································································································································</div>
      <div style="text-align: center; background-color: lightsteelblue;"><h1 style="margin: 0px;">该作者的作品</h1></div>
      <div style="text-align: center;">·····················································································································································</div>
      <div style="padding: 50px 70px;">
        <div style="display: flex; flex-wrap: wrap;">
          <LittleBook v-for="book in books" :key="book" imgName="R-C.jpg" :name="book.book_name" :rate="book.rate" :bookId="book.book_id" :userId="this.userId" style="margin: 20px;"></LittleBook>
        </div>
      </div>
    </div>
  </div>

  <el-dialog title="修改信息" v-model="dialogFormVisible" width="600px">
    <el-form :model="form">
      <el-form-item label="介绍：" label-width="150px">
        <el-input v-model="form.introduce" type="textarea" style="width: 300px;" :autosize="{minRows: 3, maxRows: 6}"></el-input>
      </el-form-item>
    </el-form>
    <div style="display: flex; justify-content: right; padding: 0px 30px;">
      <el-button @click="dialogFormVisible = false">取 消</el-button>
      <el-button type="primary" @click="modify()">确 定</el-button>
    </div>
  </el-dialog>
</template>

<script>
import LittleBook from '@/components/LittleBook.vue'
import { getUser } from '../api/user.js'
import { getAuthor, modifyAuthor } from '../api/author.js'
import { getAuthorBooks } from '../api/book.js'
import { useRoute } from 'vue-router'

export default {
  name: 'BookView',
  components: {
    LittleBook
  },
  data () {
    return {
      userId: 1,
      username: '用户',
      userType: 'manager',
      authorId: 1,
      authorName: '一个作家',
      introduce: '暂无简介',
      books: [],
      dialogFormVisible: false,
      form: { introduce: '' }
    }
  },
  mounted () {
    const route = useRoute()
    this.userId = route.query.userId
    this.authorId = route.query.authorId
    this.authorName = route.query.name
    console.log(this.userId)
    console.log(this.authorId)
    getUser(this.userId).then(res => {
      console.log(res)
      if (res.data.result === 0) {
        console.log('获取信息失败')
        return
      }
      this.username = res.data.name
      if (res.data.result.ifManager === false) this.userType = 'common'
      else this.userType = 'manager'
    })
    getAuthor(this.authorName).then(res => {
      console.log(res)
      if (res.data.result === 0) {
        this.$message.error('加载失败')
      }
      this.introduce = res.data.author.introduction
      this.form.introduce = this.introduce
    })
    getAuthorBooks(this.authorName).then(res => {
      console.log(res)
      if (res.data.result === 0) {
        this.$message.info('作者没有写书')
        return
      }
      this.books = res.data.posts
    })
  },
  methods: {
    modify () {
      modifyAuthor(this.authorId, this.form.introduce).then(res => {
        console.log(res)
        if (res.data.result === 0) {
          this.$message.error('修改信息失败')
          return
        }
        this.$message.success('成功')
        this.form = { introduce: '' }
        this.dialogFormVisible = false
      })
    }
  }
}
</script>

<style type="text/css" scoped>
.author-image-box {
  width: 150px;
  height: 200px;
  margin-left: 200px;
  margin-right: 100px;
  border: 5px solid red;
  border-style: inset;
  box-sizing: border-box;
}
.author-name {
  padding: 10px 0px;
  font-size: 40px;
  font-weight: bold;
}
.author-introduce {
  width: 440px;
  font-size: 17px;
  overflow: hidden;
  word-wrap: break-word;
  white-space: pre-line;
}
.author-introduce:hover {
  overflow-y: auto;
}
.author-modify-container {
  display: flex;
  text-align: center;
  flex-direction: column;
  justify-content: center;
  position: absolute;
  top: 145px;
  left: 1130px;
  height: 40px;
  width: 100px;
  background-color: lightgray;
  border: 3px solid rgb(153, 153, 153);
  border-radius: 10px;
}
.author-modify-container:hover {
  background-color: rgb(190, 190, 190);
  cursor: pointer;
}
.book-card:hover {
  box-shadow: 0 0 8px 8px rgb(235, 235, 235);
  cursor: pointer
}
</style>
