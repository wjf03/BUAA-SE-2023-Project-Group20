<template>
    <div class="ebook">
      <title-bar :ifSelect="ifSelect"
                  @addHighlight="addHighlight"
                  :highlightList="highlightList"
                  :colorNow="colorNow"
                  @selectColor="selectColor"
                  @removeHighlight="removeHighlight"
                  :ifInputShow="ifInputShow"
                  @showInput="showInput"
                  @finishNote="finishNote"
                  :noteList="noteList"
                  :ifNotesShow="ifNotesShow"
                  @showNotes="showNotes"
                  @hideNotes="hideNotes"
                  @updateNote="updateNote"
                  :ifLabelShow="ifLabelShow"
                  @showLabels="showLabels"
                  @hideLabels="hideLabels"
                  @addLabel="addLabel"
                  :labelList="labelList"
                  @jumpToLabel="jumpToLabel"
                  @deleteLabel="deleteLabel"
                  @jumpToNote="jumpToNote"
                  @deleteNote="deleteNote"
                  :user_id="user_id"
                  :book_id="book_id"
                  ></title-bar>
      <div class="read-wrapper">
        <div class="left" @click="prevPage">
          <span class="icon-left icon"></span>
        </div>
        <div class="middle">
          <div id="read" ></div>
        </div>
        <div class="right" @click="nextPage">
          <span class="icon-right icon"></span>
        </div>
        <div class="mask" v-if="ifMask">
          <div class="left"></div>
          <div class="center" @click="toggleSetting"></div>
          <div class="right"></div>
        </div>
      </div>
      <menu-bar :fontSizeList="fontSizeList"
              :defaultFontSize="defaultFontSize"
              @setFontSize='setFontSize'
              :themeList="themeList"
              :defaultTheme="defaultTheme"
              @setTheme="setTheme"
              :bookAvailable="bookAvailable"
              @onProgressChange="onProgressChange"
              :navigation="navigation"
              :curPercentage="curPercentage"
              @jumpTo="jumpTo"
              :parentProgress="progress"
              @addMask="addMask"
              @removeMask="removeMask"
              :ifSelect="ifSelect"
              ref="menuBar"></menu-bar>
    </div>
</template>
<script>
import TitleBar from '@/components/TitleBar'
import MenuBar from '@/components/MenuBar'
import Epub from 'epubjs'
import {getNotes, createNote, updateNoteColor, updateNoteText, deleteNote,
createLabel, getLabels, deleteLabels, getBookSource, addBook} from '@/api/api.js'
// const DOWNLOAD_URL = '/static/3.epub'
global.ePub = Epub
Date.prototype.Format = function (fmt) {
  var o = {
    'M+': this.getMonth() + 1, 
    'd+': this.getDate(), 
    'H+': this.getHours(),  
    'm+': this.getMinutes(), 
    's+': this.getSeconds(),  
    'q+': Math.floor((this.getMonth() + 3) / 3), 
    'S': this.getMilliseconds() 
  }
  if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (this.getFullYear() + '').substr(4 - RegExp.$1.length))
  for (var k in o) {
    if (new RegExp('(' + k + ')').test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length === 1) ? (o[k]) : (('00' + o[k]).substr(('' + o[k]).length)))
  }
    
  return fmt
}
export default {
  components: {
    TitleBar,
    MenuBar
  },
  data() {
    return {
      ifMask: false,
      fontSizeList: [
        {fontSize: 12},
        {fontSize: 14},
        {fontSize: 16},
        {fontSize: 18},
        {fontSize: 20},
        {fontSize: 22},
        {fontSize: 24}
      ],
      defaultFontSize: 16,
      themeList: [
        {
          name: 'default',
          style: {
            body: {
              'color': '#000', 'background': '#fff'
            }
          }
        },
        {
          name: 'eye',
          style: {
            body: {
              'color': '#000', 'background': '#ceeaba'
            }
          }
        },
        {
          name: 'night',
          style: {
            body: {
              'color': '#fff', 'background': '#000'
            }
          }
        },
        {
          name: 'gold',
          style: {
            body: {
              'color': '#000', 'background': 'rgb(241, 236, 226)'
            }
          }
        }
      ],
      highlightList: [
        // '#FFFFCC', '#CCFF99', '#CCFFFF', '#FFCCCC', '#FF6666'
        'yellow', 'green', 'blue', 'pink', 'red'
      ],
      defaultTheme: 0,
      bookAvailable: false,
      curPercentage: 0,
      navigation: {},
      progress: 0,
      ifSelect: false,
      selectRange: '',
      selectContent: '',
      colorNow: -1,
      ifInputShow: false,
      noteList: [],
      ifNotesShow: false,
      ifLabelShow: false,
      labelList: [],
      user_id: 0,
      book_id: 0,
      firstLoad: 1,
      bookURL: ''
    }
  },
  watch: {
    noteList: {
      handler (val) {
        if (this.firstLoad) {
          this.firstLoad--
        } else {
          var i =val.length
          while (i--) {
            updateNoteColor(val[i].Range, val[i].color)
            updateNoteText(val[i].Range, val[i].note)
          }
        }
      },
      deep: true
    }
  },
  methods: {
    deleteNote(index) {
      var range = this.noteList[index].Range
      this.rendition.annotations.remove(this.noteList[index].Range, 'highlight')
      this.noteList.splice(index, 1)
      deleteNote(range)
    },
    jumpToNote(index) {
      this.rendition.display(this.noteList[index].cfi)
      this.ifNotesShow = false
    },
    deleteLabel(index) {
      deleteLabels(this.labelList[index].time)
      this.labelList.splice(index, 1)
    },
    jumpToLabel(index) {
      this.rendition.display(this.labelList[index].cfi)
      this.ifLabelShow = false
    },
    addLabel() {
      console.log(this.rendition)
      console.log(this.rendition.location.start.cfi)
      var cfi = this.rendition.location.start.cfi.toString()
      var percentage = this.rendition.location.start.percentage * 100
      if (!this.labelList.find(item => item.cfi === cfi)) {
        var time = new Date().Format('yyyy-MM-dd HH:mm:ss')
        var newLabel = {'cfi': cfi, 'percentage': percentage.toFixed(0), 'time': time}
        this.labelList.push(newLabel)
        createLabel(this.user_id, this.book_id, cfi, percentage, time) 
      }
    },
    showLabels() {
      this.ifLabelShow = true
      console.log(this.labelList)
    },
    hideLabels() {
      this.ifLabelShow = false
    },
    updateNote(index, note) {
      this.noteList[index].note = note
    },
    hideNotes() {
      this.ifNotesShow = false
    },
    showNotes() {
      this.ifNotesShow = true
    },
    finishNote(note) {
      var index = this.noteList.findIndex(item => item.Range === this.selectRange)
      if (index !== -1) {
        if (this.colorNow === -1) {
          this.noteList.splice(index, 1)
        } else {
          this.noteList[index].color = this.colorNow
        }
      } else {
        if (this.colorNow !== -1) {
          var cfi = this.rendition.location.start.cfi
          console.log(typeof (this.selectRange))
          var newNote = {
            'color': this.colorNow,
            'content': this.selectContent,
            'note': note,
            'Range': this.selectRange,
            'cfi': cfi
          }
          console.log(newNote)
          this.noteList.push(newNote)
          console.log(typeof (note))
          if (note === undefined) {
            console.log(typeof (note))
            createNote(this.user_id, this.book_id, 
            this.colorNow, this.selectContent, this.selectRange, 
            '暂无', cfi)
          } else {
            createNote(this.user_id, this.book_id, 
            this.colorNow, this.selectContent, this.selectRange, 
            note, cfi)
          }
        }
      }
      this.ifMask = false
      this.ifSelect = false
      this.colorNow = -1
      this.ifInputShow = false
    },
    showInput() {
      this.ifInputShow = true
    },
    selectColor(index) {
      this.colorNow = index
    },
    addHighlight(index) {
      if (this.colorNow !== -1) {
        this.removeHighlight()
      }
      if (this.noteList.find(item => item.Range === this.selectRange)) {
        this.removeHighlight()
      } 
      this.selectColor(index)
      console.log(this.colorNow)
      this.rendition.annotations.highlight(this.selectRange, {

      }, function() {

      }, 'className', {
        'fill': this.highlightList[this.colorNow]
      })
    },
    removeHighlight() {
      this.rendition.annotations.remove(this.selectRange, 'highlight')
      this.colorNow = -1
      this.ifInputShow = false
    },
    addMask() {
      this.ifMask = true
    },
    removeMask() {
      this.ifMask = false
    },
    // 对进度条的控制
    showProgress() {
      const currentLocation = this.rendition.currentLocation()
      this.progress = this.bookAvailable ? this.locations.percentageFromCfi(currentLocation.start.cfi) : 0
      this.progress = Math.round(this.progress * 100)
    },
    // 根据链接跳转
    jumpTo(href) {
      this.rendition.display(href).then(() => {
        this.showProgress()
      })
      this.hideTitleAndMenu()
    },
    hideTitleAndMenu() {
      this.$refs.menuBar.hideSetting()
      this.$refs.menuBar.hideContent()
    },
    // 翻页，切换目录过程中给触发
    onLocationChange() {
      let curLocation = this.rendition.currentLocation()
      this.curPercentage = (Math.floor(this.locations.percentageFromCfi(curLocation.start.cfi) * 10000) / 100).toFixed(0) * 1
      this.$refs.menuBar.LocationChange()
    },
    // 进度条数值，0-100
    onProgressChange(progress) {
      const percentage = progress / 100
      const location = percentage > 0 ? this.locations.cfiFromPercentage(percentage) : 0
      this.rendition.display(location)
    },
    setTheme(index) {
      this.themes.select(this.themeList[index].name)
      this.defaultTheme = index
    },
    registerTheme() {
      this.themeList.forEach(theme => {
        this.themes.register(theme.name, theme.style)
      })
    },
    setFontSize(fontSize) {
      this.defaultFontSize = fontSize
      if (this.themes) {
        this.themes.fontSize(fontSize + 'px')
      }
    },
    toggleSetting() {
      if (this.colorNow !== -1) {
        this.finishNote()
      }
      this.ifSelect = false
      this.colorNow = -1
      this.ifInputShow = false
      this.ifNotesShow = false
      this.ifLabelShow = false
      this.$refs.menuBar.hideSetting()
    },
    prevPage() {
      // Rendition.prev
      if (this.rendition) {
        this.rendition.prev()
        this.showProgress()

        this.$refs.menuBar.hideSetting()
      }
    },
    nextPage() {
      // Rendition.next
      if (this.rendition) {
        this.rendition.next()
        this.showProgress()

        this.$refs.menuBar.hideSetting()
      }
    },
    // 电子书的解析和渲染
    showEpub() {
      console.log(this.$route.query)
      this.user_id = this.$route.query.user_id
      this.book_id = this.$route.query.book_id
      this.bookURL = this.$route.query.url
      this.href = this.$route.query.href
      this.book = Epub(this.bookURL)
      // 生成Book
      // getBookSource(this.book_id).then(respose => {
      //   this.bookURL = respose.data.result
      //   console.log(this.bookURL)
      // })

      // this.book = window.ePub(DOWNLOAD_URL)
      console.log(this.book)
      // 生成Rendition
      this.rendition = this.book.renderTo('read', {
        width: window.innerWidth - 2 * 85,
        height: window.innerHeight - 2 * 66,
        allowScriptedContent: true
      })
      getNotes(this.user_id, this.book_id).then(respose => {
        console.log(respose)
        for (var i = 0; i < respose.data.notes.length; i++) {
          var range = respose.data.notes[i].range1
          var colorIndex = parseInt(respose.data.notes[i].color)
          this.rendition.annotations.highlight(range, {

          }, function() {

          }, 'className', {
            'fill': this.highlightList[colorIndex]
          })
          var noteItem = {
            'color': colorIndex,
            'content': respose.data.notes[i].content,
            'note': respose.data.notes[i].note,
            'Range': respose.data.notes[i].range1,
            'cfi': respose.data.notes[i].cfi
          }
          this.noteList.push(noteItem)
        }
      })
      getLabels(this.user_id, this.book_id).then(respose => {
        console.log(respose)
        for (var i = 0; i < respose.data.labels.length; i++) {
          var labelItem = 
          {
            'cfi': respose.data.labels[i].cfi, 'percentage': respose.data.labels[i].percentage, 'time': respose.data.labels[i].time
          }
          this.labelList.push(labelItem)
        }
      })
      // 通过Rendition.display渲染电子书
      this.rendition.display(this.href)
      // 获取Theme对象
      this.themes = this.rendition.themes
      this.setFontSize(this.defaultFontSize)
      this.registerTheme()
      this.setTheme(this.defaultTheme)
      // 获取Location对象，通过钩子函数来实现
      this.book.ready.then(() => {
        this.navigation = this.book.navigation
        console.log(this.navigation)
        return this.book.locations.generate()
      }).then(result => {
        this.locations = this.book.locations
        this.bookAvailable = true
      })
      this.rendition.on('selected', (cfiRange, contents) => {
        console.log(cfiRange)
        this.selectRange = cfiRange
        this.selectContent = contents.window.getSelection().toString()
        if (this.selectContent !== '\n') {
          this.ifSelect = true
          this.ifMask = true
          console.log(this.selectContent)
        }
        var index = this.noteList.findIndex(item => item.Range === this.selectRange)
        if (index !== -1) {
          this.colorNow = this.noteList[index].color
        }
      })
    }
  },
  mounted() {
    this.showEpub()
  }
}
</script>
<style lang="scss" scoped>
@import 'assets/styles/global';
.ebook {
  display: flex;
  flex-direction: column;
  min-height: 100%;
  .read-wrapper {
    .left {
      position: absolute;
      left: 0;
      top: px2rem(64);
      width: px2rem(64);
      height: 90%;
      @include center;
    }
    .right {
      position: absolute;
      right: 0;
      top: px2rem(64);
      width: px2rem(64);
      height: 90%;
      @include center;
    }
    .middle {
      margin-left: px2rem(64);
      margin-right: px2rem(64);
    }
    .mask {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 100;
      display: flex;
      width: 100%;
      height: 100%;
      .left {
        flex: 0 0 px2rem(100);
      }
      .center {
        flex: 1;
      }
      .right{
        flex: 0 0 px2rem(100);
      }
    }
  }
}
</style>
