<template>
    <div id="modal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="modalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title">{{ $t(title) }}</h4>
                </div>
                <div class="modal-body">
                    {{ $t(message) }}
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" data-dismiss="modal">{{ $t(button) }}</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
 var $ = require('jquery')

 export default {
     name: 'error',
     data: function () {
         return {
             title: 'Error',
             message: '',
             button: 'Close'
         }
     },
     mounted: function (msg) {
         this.$bus.$on('error', this.alert)
     },
     methods: {
         alert: function (msg) {
             this.message = msg
             $('#modal').modal({
                 backdrop: 'static'
             })
         }
     }
 }
</script>
