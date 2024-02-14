-- Store the computed average score back into the users table
-- Compute the average score for the given user_id

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser @userId INT AS
BEGIN
    DECLARE avgScore FLOAT;

    SELECT avgScore = AVG(score)
    FROM scores
    WHERE user_id = @userId;

    UPDATE users
    SET @averageScore
    WHERE id = @userId;
END;
//
DELIMITER;
