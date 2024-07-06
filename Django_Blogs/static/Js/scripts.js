$(document).ready(function() {
    $('#commentForm').on('submit', function(event) {
        event.preventDefault();
        console.log('Button Clicked');

        let comment_text = $('#comment').val();
        let csrf = $("input[name=csrfmiddlewaretoken]").val();
        console.log(comment_text);
        let mydata = {
            text: comment_text,
            csrfmiddlewaretoken: csrf
        };

        $.ajax({
            url: window.location.href,
            method: "POST",
            data: mydata,
            success: function(data) {
                console.log(data);
                let comments = data.comment_data;
                if (data.status === "Save") {
                    console.log("Form Submitted");
                    $("form")[0].reset();

                    let output = '';  // Initialize the output variable

                    comments.forEach(function(comment) {
                        let canDelete = comment.is_host;

                        output += `
                            <div class="comment">
                                <div class="comment-header">
                                    <p class="comment-author">@${comment.host} --  Date : ${comment.created}</p>
                                </div>
                                <div class="comment-body">
                                    <p>${comment.text}</p>
                                </div>
                                <div class="comment-actions">
                                    ${canDelete ? `
                                        <div class="delete-button">
                                            <a class="delete-btn" href="/delete-comment/${comment.id}/">Delete</a>
                                        </div>
                                    ` : ''}
                                </div>
                            </div>
                        `;
                    });

                    // Append the new comments HTML to the comments section
                    $('#comments-section').html(output);

                } else if (data.status === 0) {
                    console.log("Not Submitted");
                }
            },
            error: function(xhr, status, error) {
                // Handle any errors that occur during the AJAX request
                $('#comments-section').html('Error fetching data: ' + error);
            }
        });
    });
});
