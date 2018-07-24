//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    motto: 'Hello World',
    userInfo: {},
    img_arr:[],
    name_api:[],
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo')
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  },
  bindChooseImage: function(){
    var that = this
    var mask_value = true
    wx.chooseImage({
      success: function (res) {
        var tempFilePaths = res.tempFilePaths;
        that.setData({
          img_arr: that.data.img_arr.concat(res.tempFilePaths),
          imgUrl:tempFilePaths,
        })
        var tempFilePaths = res.tempFilePaths
        wx.uploadFile({
          url: 'https://ai.kilig.com.cn/test/', 
          filePath: tempFilePaths[0],
          name: 'picture',

          success: function (res) {
            var data = res.data
            var json_data = JSON.parse(res.data)
            that.setData({
              name_api: that.data.name_api.concat(json_data['name']),
              name_img:json_data['name'],
              length_api:that.data.name_api.length,
            })
          }
          
        })
        wx.showToast({
          title: '图片识别中...',
          icon: 'loading',
          mask: true,
          duration: 15000
        })

      }
    })
  },
})

