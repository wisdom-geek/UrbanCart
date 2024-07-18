console.log("working fine");


const monthNames = Array.from({ length: 12 }, (e, i) =>
  new Date(0, i).toLocaleString("en-US", { month: "short" })
);

$("#commentForm").submit(function (e) {
  e.preventDefault();

  let date = new Date();
  let time =
    date.getDay() +
    " " +
    monthNames[date.getUTCMonth()] +
    ", " +
    date.getUTCFullYear();
  // Client-side validation (example)
  let reviewText = $("textarea[name='review']").val();
  if (reviewText.trim() === "") {
    $("#review-res").html("Review cannot be empty.");
    return;
  }

  $.ajax({
    data: $(this).serialize(),
    method: $(this).attr("method"),
    url: $(this).attr("action"),
    dataType: "json",
    headers: { "X-CSRFToken": "{{ csrf_token }}" }, // Include CSRF token for security
    success: function (res) {
      console.log("Comment saved to Db");

      if (res.bool === true) {
        $("#review-res").html("Review added successfully.");
        $(".hide-comment-form").hide();
        $(".add-review").hide();

        let _html =
          '<div class="single-comment justify-content-between d-flex mb-30">';
        _html += '<div class="user justify-content-between d-flex">';
        _html += '<div class="thumb text-center">';
        _html +=
          '<img src="https://www.shutterstock.com/image-vector/vector-flat-illustration-grayscale-avatar-600nw-2264922221.jpg" alt="" />';
        _html +=
          '<a href="#" class="font-heading text-brand">' +
          res.context.user +
          "</a>";
        _html += "</div>";

        _html += '<div class="desc">';
        _html += '<div class="d-flex justify-content-between mb-10">';
        _html += '<div class="d-flex align-items-center">';
        _html += '<span class="font-xs text-muted">' + time + "</span>";
        _html += "</div>";

        for (let i = 1; i <= res.context.rating; i++) {
          _html += '<i class="fas fa-star text-warning"></i>';
        }

        _html += "</div>";
        _html += '<p class="mb-10">' + res.context.review + "</p>";

        _html += "</div>";
        _html += "</div>";
        _html += "</div>";
        $(".comment-list").prepend(_html);
      }
    },
    error: function (xhr, status, error) {
      console.log("Error saving comment: " + error);
      $("#review-res").html(
        "An error occurred while saving your review. Please try again."
      );
    },
  });
});

$(document).ready(function(){
    $(".filter-checkbox, #price-filter-btn").on("click", function(){
        // console.log('This checkbox has been clicked');

        let filter_object = {}
        let min_price = $("#max_price").attr("min")
        let max_price = $("#max_price").val()

        filter_object.min_price =min_price;
        filter_object.max_price = max_price

        $(".filter-checkbox").each(function(){
            let filter_value = $(this).val()

            let filter_key = $(this).data("filter")
            // console.log("Filter value is", filter_value)
            // console.log("Filter value is", filter_key)

            filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter='+ filter_key +']:checked')).map(function(element){
                return element.value
            })
        })
        // console.log("Filter object is", filter_object);
        $.ajax({
            url: '/filter-products',
            data: filter_object,
            dataType: 'json',
            beforeSend: function(){
                console.log("Trying to filter products ")
            },
            success: function(response){
                console.log(response) 
                console.log('Data filtered successfully')
                $("#filtered-product").html(response.data) 
            }

        })
    });
    $("#max_price").on("blur", function(){
        let min_price = $(this).attr("min")
        let max_price = $(this).attr("max")
        let current_price= $(this).val()      

        if(current_price < parseInt(min_price) || current_price > parseInt(max_price)){          
            
            min_price = Math.round(min_price * 100 )/100
            max_price = Math.round(max_price * 100 )/100

           alert("Price must be between $"+ min_price + " and $" + max_price)
           
           
           $(this).val(min_price)
           $('#range').val(min_price)
           $(this).focus()

           return false

        }
    })
});


