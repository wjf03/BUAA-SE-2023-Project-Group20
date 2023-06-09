<template>
  <div style="background-color: aliceblue;">
    <div style="margin-left: 160px; margin-right: 160px;">
      <div style="background-color: lightblue; padding-top: 40px; padding-bottom: 10px;">
        <img class="book-image-box" src="@/assets/book.png" alt="img"/>
        <div style="display: inline-block; vertical-align: top;">
          <div class="book-title">{{ bookName }}</div>
          <el-rate v-model="rate" disabled show-score score-template="{value}"/>
          <div class="book-author">作者：<span class="author-name" @click="authorInfo(authorId)" style="text-decoration: underline">{{ authorName }}</span></div>
          <div class="book-label"><span>{{ label1 }}</span></div>
          <div class="book-label"><span>{{ label2 }}</span></div>
          <el-scrollbar max-height="160px" style="margin: 10px 0px;">
            <div class="book-introduce">{{ introduce }}</div>
          </el-scrollbar>
        </div>
        <div v-if="userType == 'manager'" class="book-modify-container" @click="dialogFormVisible = true">
          <span>修改信息</span>
        </div>
        <div v-else class="book-star-container" @click="star()">
          <div v-if="isStar">已收藏</div>
          <div v-else>+收藏</div>
        </div>
      </div>
      <div style="text-align: center;">·····················································································································································</div>
      <div style="text-align: center; background-color: lightsteelblue;"><h1 style="margin: 0px;">分节阅读</h1></div>
      <div style="text-align: center;">·····················································································································································</div>
      <el-scrollbar max-height="300px" style="background-color: lightblue;">
        <div class="chapter-info-container" v-for="(chapter, index) in chapters" :key="chapter" @click="readBook(index)">
          <el-text size="large" truncated>{{ chapter.chapter_name }}</el-text>
        </div>
      </el-scrollbar>
      <div style="text-align: center;">·····················································································································································</div>
      <div style="text-align: center; background-color: lightsteelblue;"><h1 style="margin: 0px;">用户评论</h1></div>
      <div style="text-align: center;">·····················································································································································</div>
      <div class="comment-container">
        <el-scrollbar max-height="600px" class="comment-container">
          <el-card v-for="comment in comments" :key="comment" shadow="hover" style="margin: 5px;">
            <template #header>
              <div style="display: flex;">
                <p style="display: flex; flex-direction: column; justify-content: center; margin: 0px;">{{ comment["username"] }}</p>
                <el-rate v-model='comment["rate"]' disabled show-score score-template="{value}" style="margin-left: auto;"/>
              </div>
            </template>
            <el-text>
              {{ comment["content"] }}
            </el-text>
          </el-card>
        </el-scrollbar>
      </div>
      <div class="comment-input-container">
        <el-input v-model="comment_input" placeholder="输入评论……（最多300字）" :autosize="{minRows: 3, maxRows: 6}" type="textarea" maxlength="300" show-word-limit/>
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 10px 5px 5px 5px;">
          <span style="display:inline-block;">评分：</span>
          <el-rate v-model="comment_input_rate" show-score score-template="{value}"></el-rate>
          <el-button type="default" @click="comment" style="display: inline-block; margin-left: auto;">发表评论</el-button>
        </div>
      </div>
    </div>
  </div>

  <el-dialog title="修改信息" v-model="dialogFormVisible" width="600px">
    <el-form :model="form">
      <el-form-item label="书名：*" label-width="150px">
        <el-input v-model="form.bookName" autocomplete="off" style="width: 180px;"></el-input>
      </el-form-item>
      <el-form-item label="作者：*" label-width="150px">
        <el-input v-model="form.author" autocomplete="off" style="width: 180px;"></el-input>
      </el-form-item>
      <el-form-item label="主类别*" label-width="150px">
        <el-select v-model="form.label1" placeholder="请选择主类别" style="width: 180px;">
          <el-option v-for="item in firstLabels" :key="item.value" :value="item.value">{{ item.value }}</el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="副类别*" label-width="150px">
        <el-select v-model="form.label2" placeholder="请选择主类别" style="width: 180px;">
          <el-option v-for="item in getLabels(form.label1)" :key="item" :value="item">{{ item }}</el-option>
        </el-select>
      </el-form-item>
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
import { addStar, deleteStar, listStar } from '../api/star.js'
import { getBookById, modifyBook, modifyRate } from '../api/book.js'
import { addComment, searchComment } from '../api/comment.js'
import { getUser } from '../api/user.js'
import { getAuthor, addAuthor } from '@/api/author.js'
import { getChapters } from '../api/chapter.js'
import { useRoute } from "vue-router";

export default {
  name: 'BookView',
  data () {
    return {
      userId: 1,
      username: '用户',
      userType: 'common',
      bookId: 1,
      bookName: '一本书',
      bookType: 'common',
      rate: 0,
      authorId: 1,
      authorName: '一个作者',
      isStar: false,
      label1: '历史',
      label2: '中国历史',
      bookURL: '',
      introduce: '暂无介绍',
      chapters: [],
      comment_input: '',
      comment_input_rate: 0,
      comments: [],
      dialogFormVisible: false,
      firstLabels: [{
        value: '哲学',
        includes: ['政治哲学', '伦理学', '认识论哲学', '逻辑学', '其他']
      },
      {
        value: '自然科学',
        includes: ['数学', '物理学', '化学', '生物学', '其他']
      },
      {
        value: '历史',
        includes: ['中国历史', '世界历史', '其他']
      },
      {
        value: '文学',
        includes: ['小说', '散文', '曲艺', '童话', '诗歌', '其他']
      },
      {
        value: '艺术',
        includes: ['艺术理论', '绘画', '音乐', '舞蹈', '其他']
      },
      {
        value: '应用科学',
        includes: ['计算机科学', '天文学', '农业科学', '其他']
      },
      {
        value: '其他',
        includes: ['其他']
      }],
      form: {
        bookName: '',
        author: '',
        label1: '',
        label2: '',
        introduce: ''
      }
    }
  },
  mounted () {
    console.log(this.$route.params.id)
    this.bookId = this.$route.params.id
    const route = useRoute();
    this.userId = route.query.userId;
    getUser(this.userId).then(res => {
      console.log(res)
      if (res.data.result === 0) {
        console.log('获取信息失败')
        return
      }
      this.username = res.data.name
      if (res.data.result.ifManager === false) this.userType = 'common'
      else this.userType = 'manager'
      getBookById(this.$route.params.id).then(res => {
        console.log(res)
        if (res.data.result === 0) {
          console.log('获取信息失败')
          return
        }
        this.bookId = res.data.post.book_id
        this.bookName = res.data.post.book_name
        this.rate = res.data.post.book_score
        this.authorName = res.data.post.book_author_name
        this.label1 = res.data.post.book_main_type
        this.label2 = res.data.post.book_secondary_type
        this.introduce = res.data.post.book_introduction
        this.bookURL = res.data.post.book_url
        this.popularity = res.data.post.book_popularity
        this.form = { bookName: this.bookName, author: this.authorName, label1: this.label1, label2: this.label2, introduce: this.introduce }
        if (this.authorName) {
          getAuthor(this.authorName).then(res => {
            console.log(res)
            if (res.data.result === 0) return
            this.authorId = res.data.author.id
          })
        }
        getChapters(this.$route.params.id).then(res => {
          console.log(res)
          if (res.data.result === 0) {
            this.$message.error('获取章节失败')
            return
          }
          this.chapters = res.data.posts
          console.log(this.chapters)
          searchComment(this.$route.params.id).then(res => {
            console.log(res)
            if (res.data.result === 0) {
              this.$message.info('无评论')
              return
            }
            for (let index = 0; index < res.data.comments.length; index++) {
              const element = res.data.comments[index]
              let n = ''
              getUser(element.user_id).then(r => {
                console.log(r)
                n = r.data.result.name
                console.log(n)
                const com = { username: n, rate: element.rate, content: element.content }
                console.log(com)
                this.comments.push(com)
              })
            }
            listStar(this.userId).then(res => {
              console.log(res)
              for (let index = 0; index < res.data.stars.length; index++) {
                const element = res.data.stars[index]
                if (element.book_id - this.bookId === 0) {
                  this.isStar = true
                  return
                }
              }
              this.isStar = false
            })
          })
        })
      })
    })
  },
  methods: {
    star () {
      this.isStar = !this.isStar
      if (this.isStar) {
        addStar(this.userId, this.bookId).then(res => {
          console.log(res)
          if (res.data.result === 0) {
            this.$message.error('失败！')
            return
          }
          this.$message.success('收藏成功！')
        })
      } else {
        deleteStar(this.userId, this.bookId).then(res => {
          console.log(res)
          if (res.data.result === 0) {
            this.$message.error('失败！')
            return
          }
          this.$message.success('取消收藏成功！')
        })
      }
    },
    modify () {
      if (this.form.bookName === '') {
        this.$message.error('书名不能为空')
        return
      }
      this.$message.info('正在修改信息')
      modifyBook(this.bookId, this.form.bookName, this.form.label1, this.form.label2, this.form.introduce, this.form.author).then(res => {
        console.log(res)
        console.log(this.form)
        if (res.data.result === 0) {
          this.$message.error('失败！')
          return
        }
        getAuthor(this.form.author).then(res => {
          console.log(res)
          if (res.data.result === 0) {
            addAuthor(this.form.author, '暂无简介').then(r => {
              console.log(r)
              
            })
          }
        })
        this.$message.success('修改成功')
      })
      this.dialogFormVisible = false
    },
    authorInfo (id) {
      console.log(this.authorId)
      this.$router.push({ path: '/author/' + id, query: { userId: this.userId, authorId: this.authorId, name: this.authorName } })
    },
    readBook (index) {
      const path = window.location.protocol + '//' + 'localhost:8080/#/ebook?user_id=' + this.userId + '&book_id=' + this.bookId + '&url=' + this.bookURL + '&href=' + this.chapters[index].chapter_href
      window.location.href = path
    },
    comment () {
      if (this.comment_input === '') {
        this.$message.error('评论不能为空！')
        return
      }
      addComment(this.userId, this.bookId, this.comment_input_rate, this.comment_input).then(res => {
        console.log(res)
        if (res.data.result === 0) {
          this.$message.error('评论失败')
          return
        }
        this.$message.success('评论成功！')
        this.comment_input = ''
        this.comment_input_rate = 0
        var score = 0
        for (let index = 0; index < this.comments.length; index++) {
          const element = this.comments[index];
          score = score + element.rate
        }
        modifyRate(this.bookId, Math.round(score/(this.comments.length))).then(res => {
          console.log(res)
        })
      })
    },
    getLabels (theValue) {
      for (let index = 0; index < this.firstLabels.length; index++) {
        const element = this.firstLabels[index]
        if (theValue === element.value) {
          return element.includes
        }
      }
      return []
    }
  }
}
</script>

<style type="text/css" scoped>
.book-image-box {
  width: 225px;
  height: 300px;
  margin-left: 120px;
  margin-right: 100px;
  border: 5px solid red;
  border-style: inset;
  box-sizing: border-box;
}
.book-title {
  margin: 10px 0px;
  font-size: 40px;
  font-weight: bold;
}
.book-author {
  margin: 10px 0px;
  font-size: 20px;
  color: #2828eb;
}
.author-name {
  text-decoration: underline;
}
.author-name:hover {
  cursor: pointer;
  text-shadow: 1px 1px 3px blue;
}
.book-label {
  display: inline;
  text-align: center;
  font-size: 18px;
  margin: 0px 8px;
  padding: 3px 6px;
  background-color: orange;
  border-radius: 7px;
}
.book-introduce {
  width: 440px;
  font-size: 17px;
  overflow: hidden;
  word-wrap: break-word;
  white-space: pre-line;
}
.book-introduce:hover {
  overflow-y: auto;
}
.book-star-container {
  display: flex;
  text-align: center;
  flex-direction: column;
  justify-content: center;
  position: absolute;
  top: 145px;
  left: 1130px;
  height: 40px;
  width: 100px;
  background-color: pink;
  border: 3px solid rgb(255, 142, 160);
  border-radius: 10px;
}
.book-star-container:hover {
  background-color: rgb(255, 177, 190);
  cursor: pointer;
}
.book-modify-container {
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
.book-modify-container:hover {
  background-color: rgb(190, 190, 190);
  cursor: pointer;
}
.chapter-info-container {
  height: 30px;
  margin: 3px 5px;
  padding-left: 8px;
  border-color: blue;
  border-style: solid;
  border-width: 2px;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
}
.chapter-info-container:hover {
  background-color: rgba(0, 0, 0, 0.1);
  cursor: pointer;
}
.comment-container {
  background-color: rgb(240, 240, 240);
}
.comment-input-container {
  background-color: rgb(240, 240, 240);
  padding: 10px 5px 5px 5px;
  border-top-color: lightgray;
  border-width: 1px 0px 0px 0px;
  border-style: solid;
}
/deep/ .el-rate__icon {
  font-size: 30px;
}
/deep/ .el-card .el-rate__icon {
  font-size: 20px;
}
/deep/ .comment-input-container .el-rate__icon {
  font-size: 20px;
}
/deep/ .el-rate__text {
  font-size: 20px;
}
/deep/ .el-card .el-rate__text {
  font-size: 17px;
}
/deep/ .comment-input-container .el-rate__icon {
  font-size: 17px;
}
.el-card__body .el-text{
  font-size: 17px;
}
/deep/ .el-textarea__inner {
  font-size: 17px;
}
</style>
