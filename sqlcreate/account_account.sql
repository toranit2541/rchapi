USE [Ruamchai]
GO

/****** Object:  Table [dbo].[account_account]    Script Date: 11/26/2024 1:22:37 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[account_account](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[gender] [nvarchar](10) NOT NULL,
	[birthday] [datetimeoffset](7) NOT NULL,
	[phonenumber] [nvarchar](10) NULL,
	[user_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[account_account]  WITH CHECK ADD  CONSTRAINT [account_account_user_id_8d4f4816_fk_auth_user_id] FOREIGN KEY([user_id])
REFERENCES [dbo].[auth_user] ([id])
GO

ALTER TABLE [dbo].[account_account] CHECK CONSTRAINT [account_account_user_id_8d4f4816_fk_auth_user_id]
GO


